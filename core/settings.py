from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database settings
    MONGO_URI: str
    MONGO_DB: str
    MONGO_COLLECTION: str
    MONGO_DEFAULT_COLLECTION: str = "tareas"
    
    class Config:
        env_file = ".env"
        extra = "allow"
settings = Settings()
