from pydantic import BaseSettings


class Settings(BaseSettings):
    CELERY_BACKEND: str = 'redis://:localhost:6379/0'
    CELERY_BROKER: str = 'redis://:localhost:6379/1'


settings = Settings()
