from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    pokeapi_base_url: str = "http://pokeapi.co/api/v2"
    title: str
    host: str
    port: int
    class Config:
        env_file = ".env"

settings = Settings()
