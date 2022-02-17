from pydantic import BaseSettings


class Settings(BaseSettings):
    CELERY_BACKEND: str = 'redis://:localhost:6379/0'
    CELERY_BROKER: str = 'amqp://qwerty:12qwaszx@localhost:5672//'


settings = Settings()
