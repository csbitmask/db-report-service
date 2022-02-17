from celery import Celery

from .config.settings import settings

celery_app = Celery(
    'dbr_worker',
    backend=settings.CELERY_BACKEND,
    broker=settings.CELERY_BROKER
)

celery_app.conf.task_routes = {
    "app.tasks.test_task.test_celery": "test-queue"}
