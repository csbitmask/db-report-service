from celery import Celery

from .config.settings import settings

celery_app = Celery(
    'shiva_worker',
    backend=settings.CELERY_BACKEND,
    broker=settings.CELERY_BROKER
)

# TODO: configure routing
