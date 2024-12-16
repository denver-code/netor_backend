from pydantic_settings import BaseSettings


class Config(BaseSettings):
    PROJECT_NAME: str = "netor_app"
    # DATABASE_NAME: str = "netor"
    # DATABASE_URL: str = "mongodb://localhost:27017"

    class Config:
        case_sensitive = True
        env_file = ".env"


config = Config()
