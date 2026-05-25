from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status as statuscode
import uvicorn
import logfire
from settings import api_settings
from contextlib import asynccontextmanager
import asyncio
import asyncio
from store import initialize_store, _types, _pokemon, list_types, list_pokemon


# diego in Jan 2025
__all__ = ("app", "run")

from routers import router

app = FastAPI(
    title=api_settings.title, version="0.0.0"
)


origins = ["*"]




app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
    allow_headers=['Origin',
      'X-Requested-With',
      'Content-Type',
      'Accept',
      'Authorization',
      'X-XSRF-TOKEN',
      "Access-Control-Allow-Origin"],
)



def main():
    # Initialize the in-memory store - this will fetch data from PokeAPI and populate the _types and _pokemon dictionaries.
    print ("Initializing store with data from PokeAPI...")
    asyncio.run(initialize_store())

    # Access the collections to verify initialization
    #print("Types:", _types)
    #print("Pokemon:", _pokemon)
    print("Store initialization complete.")

    print ("access the collections to verify initialization")
     # Access the collections to verify initialization
    print("Types:", list_types())
    print("Pokemon:", list_pokemon())
    

if __name__ == "__main__":
    main()
    uvicorn.run(app, host=api_settings.host, port=api_settings.port)
