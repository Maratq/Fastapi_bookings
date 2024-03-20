from pydantic import model_validator


class Settings:
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_NAME: str
    DB_PASS: str

    @model_validator
    def get_database_url(cls, v):
        v["DATABASE_URL"] = (
            f"postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASS']}@{v['DB_HOST']}/{v['DB_NAME']}"
        )
        return v

    SECRET_KEY: str
    ALGORITHM: str
    
    class Config:
        env_file = ".env"


settings = Settings()
