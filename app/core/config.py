from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    PROJECT_NAME: str = "Todo List API"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    DATABASE_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/todo_app.db"

    SECRET_KEY: str = "DEV_ONLY_SECRET_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

settings = Settings()