from pydantic import BaseSettings


class Settings(BaseSettings):
    CELERY_WORKER_NAME: str = 'celery_worker'
    CELERY_BACKEND: str = 'redis://localhost:6379'
    CELERY_BROKER: str = 'pyamqp://qwerty:12qwaszx@localhost:5672//'


settings = Settings()
