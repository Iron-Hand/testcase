from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Account


logger = get_task_logger(__name__)


@shared_task
def fix_hold_task():
    list = Account.objects.filter(status='Open')
    for account in list:
        account.fix_hold()
    logger.info("The fix hold task just ran.")
