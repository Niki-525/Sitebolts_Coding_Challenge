"""
API Service Module

Add relevant logic that can be abstracted away from the route method to the challenge here

"""
#--------------------service.py---------------------------------------------
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import httpx
from fastapi import HTTPException
from schemas import TypeCreate, TypeOut, PokemonCreate, PokemonOut
from store import _types, _pokemon, next_type_id, next_pokemon_id
from settings import api_settings
async def _fetch_from_pokeapi(path: str) -> dict:
    """
    Single async httpx call to PokeAPI.
    Raises 404 HTTPException if PokeAPI returns 404.
    Raises 502 for any other upstream error (bad gateway — their API issue, not our problem).
    """
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(f"{api_settings.pokeapi_base_url}/{path}")
        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"PokeAPI is unreachable: {e}")
        if r.status_code == 404:
            raise HTTPException(status_code=404, detail=f"'{path}' not found in PokeAPI")
        if r.status_code != 200:
            raise HTTPException(status_code=502, detail=f"PokeAPI returned {r.status_code}")
        return r.json()

# Type services
async def create_type(body: TypeCreate) -> TypeOut:
    """
    Accepts a request body and inserts a new Pokémon type into the store.
    Returns the created type with its generated ID.
    Returns 409 if a type with that name already exists.
    """
    # 1. Check if the type already exists in the store
    for type_id, existing in _types.items():
        if existing["name"].lower() == body.name.lower():
            raise HTTPException(
                status_code=409,
                detail=f"Type '{body.name}' already exists with ID {type_id}"
            )

    # 2. Assign a new ID from the counter and insert into the store
    new_id = next_type_id()
    record = {"id": new_id, "name": body.name.lower()}
    _types[new_id] = record

    # 3. Return the created type
    return TypeOut(**record)


    # GET /types logic; read from store; no I/O
    #return [TypeOut(**t) for t in store._types.values()]
    #t = list_types()
    #return TypeOut(**t)

def list_typesfromStore() -> list[TypeOut]:
    return [TypeOut(id=key, name=value["name"]) for key, value in _types.items()]

# Pokemon services
async def create_pokemon(body: PokemonCreate) -> PokemonOut:
       # Check if type_id exists in the store
    parent_type = _types.get(body.type_id)
    if parent_type is None:
        raise HTTPException(
            status_code=404,
            detail=f"Type ID {body.type_id} not found"
        )

    # Insert the Pokémon into the store
    new_id = next_pokemon_id()
    record = {
        "id": new_id,
        "name": body.name.lower(),
        "type_id": body.type_id,
        "height": 10,  # Example static value, replace with actual logic if needed
        "weight": 100,  # Example static value, replace with actual logic if needed
        "base_experience": 50,  # Example static value, replace with actual logic if needed
    }
    _pokemon[new_id] = record

    # Return the created Pokémon with the resolved type name
    return PokemonOut(**record, type_name=parent_type["name"])

def list_pokemon() -> list[PokemonOut]:
    """
    GET /pokemon logic
    Resolve type_name for every pokemon via the store
    """
    result = []
    for key, p in _pokemon.items():
        parent_type = _types.get(p["type_id"])
        type_name = parent_type["name"] if parent_type else "unknown"
        result.append(
            PokemonOut(
                id=key,
                name=p["name"],
                type_id=p["type_id"],
                type_name=type_name,
                height=p["height"],
                weight=p["weight"],
                base_experience=p.get("base_experience"),
            )
        )
    return result