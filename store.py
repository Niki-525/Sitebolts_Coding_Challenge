"""
In-Memory Store

This module simulates a database using module-level dicts.
State resets on every server restart — no persistence layer required.

There are two collections with a foreign key-style relationship:
    - _types: stores pokemon types (the "parent" table)
    - _pokemon: stores pokemon, each referencing a type by ID (the "child" table)

Use the counter helpers to generate unique IDs for new records.
"""

_types: dict[int, dict] = {}
_pokemon: dict[int, dict] = {}
_type_counter: int = 0
_pokemon_counter: int = 0


def next_type_id() -> int:
    global _type_counter
    _type_counter += 1
    return _type_counter


def next_pokemon_id() -> int:
    global _pokemon_counter
    _pokemon_counter += 1
    return _pokemon_counter

import httpx
import asyncio

async def initialize_store():
    global _types, _pokemon

    async with httpx.AsyncClient() as client:
        # Fetch and populate _types from PokeAPI - I am just going to set the limit to 10000 to get all the types, but in a real application we might want to limit this or paginate through results.
        types_response = await client.get("https://pokeapi.co/api/v2/type?limit=21")  # Fetch all types
        if types_response.status_code == 200:
            types_data = types_response.json().get("results", [])
            for type_data in types_data:
                _types[next_type_id()] = {"name": type_data["name"]}
        else:
            print("Failed to fetch types from PokeAPI")

        # Fetch and populate _pokemon from PokeAPI - I am just going to set the limit to 10000 to get all the pokemon, but in a real application we might want to limit this or paginate through results.
        pokemon_response = await client.get("https://pokeapi.co/api/v2/pokemon?limit=10")  # Fetch first 10 Pokemon
        if pokemon_response.status_code == 200:
            pokemon_data = pokemon_response.json().get("results", [])
            for pokemon in pokemon_data:
                # Fetch detailed data for each Pokemon to get its type(s)
                pokemon_detail_response = await client.get(pokemon["url"])
                if pokemon_detail_response.status_code == 200:
                    pokemon_detail = pokemon_detail_response.json()
                    type_ids = []
                    for pokemon_type in pokemon_detail["types"]:
                        # Match the type name with _types to get the type_id
                        type_name = pokemon_type["type"]["name"]
                        type_id = next((id for id, t in _types.items() if t["name"] == type_name), None)
                        if type_id:
                            type_ids.append(type_id)

                    # Add the Pokemon to _pokemon with the first type_id (if available)
                    if type_ids:
                        _pokemon[next_pokemon_id()] = {"name": pokemon["name"], "type_id": type_ids[0],"type_name":type_name ,"height": pokemon_detail["height"], "weight": pokemon_detail["weight"], "base_experience": pokemon_detail.get("base_experience")}
        else:
            print("Failed to fetch Pokemon from PokeAPI")

def list_types():
    return _types
def list_pokemon():
    return _pokemon