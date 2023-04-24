from functools import lru_cache
from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    SESSION_SECRET_KEY: str = 'secretkey'
    CORS_ORIGINS: str = '*'

    KEYDB_URL: str
    KEYDB_PASSWORD: SecretStr

    class Config:
        env_file = 'complexity_app/.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_settings(**kwargs):
    return Settings(**kwargs)
