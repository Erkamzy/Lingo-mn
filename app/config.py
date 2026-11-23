from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "LingoMN"
    database_url: str = "sqlite:///lingomn.db"
    secret_key: str = "change-me"

settings = Settings()