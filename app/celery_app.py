from celery import Celery

from .config.settings import settings

celery_app = Celery(
    'shiva_worker',
    backend=settings.CELERY_BACKEND,
    broker=settings.CELERY_BROKER
)

celery_app.conf.task_routes = {
    "app.worker.celery_worker.test_celery": "test-queue"}
