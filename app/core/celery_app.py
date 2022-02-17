from time import sleep

from celery import Celery
from celery.utils.log import get_task_logger

from app.core.settings import settings

celery_app = Celery(
    settings.CELERY_WORKER_NAME,
    backend=settings.CELERY_BACKEND,
    broker=settings.CELERY_BROKER
)

celery_log = get_task_logger(__name__)


@celery_app.task
def create_order(name, quantity):
    # 5 seconds per 1 order
    complete_time_per_item = 5

    # Keep increasing depending on item quantity being ordered
    sleep(complete_time_per_item * quantity)  # Display log
    celery_log.info(f"Order Complete!")
    return {"message": f"Hi {name}, Your order has completed!",
            "order_quantity": quantity}
