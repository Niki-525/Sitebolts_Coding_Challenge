
"""
API Router

Add route and REST API methods for the challenge here.

"""
from fastapi import APIRouter, BackgroundTasks
from schemas import TypeCreate, TypeOut, PokemonCreate, PokemonOut
from services import api_service
router = APIRouter(prefix="/process")


# ROUTES GO HERE

# --- External API objective ---
# Add endpoints that fetch and return data from PokeAPI (or an API of your choosing).
# Each endpoint should return a structured Pydantic response model.
# --- Data modeling objective ---
# Implement the following four endpoints using the in-memory store in store.py.
# Define whatever Pydantic schemas you need in schemas.py and business logic in services/api_service.py.
#
# POST /process/types
#   - Accept a request body and insert a new pokemon type into the store
#   - Return the created type with its generated ID
#   - Return 409 if a type with that name already exists
@router.post("/types", response_model=TypeOut, status_code=201)
async def post_type(body: TypeCreate):
    """ insert a new pokemon type into the store. 
    validates the name against pokeAPI before storing.
    Returns 409 if the type name already exists"""
    return await api_service.create_type(body)

# GET /process/types
#   - Return a list of all pokemon types in the store
@router.get("/types", response_model=list[TypeOut])
def get_types():
    return api_service.list_typesfromStore()

# POST /process/pokemon
#   - Accept a request body and insert a new pokemon into the store
#   - Each pokemon must reference an existing type by ID (enforced by you, not the DB)
#   - Return 404 if the referenced type ID does not exist
#   - The response should include the type name resolved from the store (not just the ID)
#
@router.post("/pokemon", response_model=PokemonOut, status_code=201)
async def post_pokemon(body: PokemonCreate):
    """ insert a new pokemon into the store. 
    Each pokemon must reference an existing type by ID (enforced by you, not the DB).
    Return 404 if the referenced type ID does not exist.
    The response should include the type name resolved from the store (not just the ID)"""
    return await api_service.create_pokemon(body)
# GET /process/pokemon
#   - Return a list of all pokemon, with each entry including its resolved type name
@router.get("/pokemon", response_model=list[PokemonOut])
def get_pokemon():
    return api_service.list_pokemon()
