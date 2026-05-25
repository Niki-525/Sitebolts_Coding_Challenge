"""
Schemas 

Add relevant Pydantic models and schemas for request validation and response serialization.
These define the structure and validation rules for your data.

"""

from typing import Annotated, Optional, Tuple, List, Dict, Any
from pydantic import BaseModel
#Type Schemas
class TypeCreate(BaseModel):
    name: str 
class TypeOut(BaseModel):
    id: int
    name: str
#Pokemon Schemas
class PokemonCreate(BaseModel):
    name: str
    type_id: int
class PokemonOut(BaseModel):
    id: int
    name: str #i didnt see a name so i am inserting it here.
    type_id: int
    type_name: str
    height: int
    weight: int
    base_experience: Optional[int]= None
