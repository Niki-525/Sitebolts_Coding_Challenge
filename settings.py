"""SETTINGS
Settings loaders using Pydantic BaseSettings classes
(load from environment variables / dotenv file)
"""

import os
import json
from typing import List, Dict, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
import logfire
__all__ = ("api_settings")




class APISettings(BaseSettings):
    """General application settings"""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    title: str ="Sitepolts FastAPI Coding Challenge"
    host: str = "127.0.0.1"
    port: int = 8000
    log_level: str = "INFO"


api_settings = APISettings()

