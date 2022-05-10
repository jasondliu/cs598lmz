import gc, weakref
from django.db import models

from .signals import cron_worker_started, cron_worker_finished
from .exceptions import CronTaskException
from .utils import class_path_of, class_instance_method
from .settings import cron_manager_settings
from .models import CronTask
from .app_settings import UPDATE_CRON_TASK_STATUS_ONLY_ON_SUCCESS


def register_crontab_tasks():
    """
    Goes through all the registered crontab tasks and registers them.
    """

    # First, unregister any tasks that have been removed.
    tasks = CronTask.objects.all()
    registered_task_ids = [task.id for task in tasks]
    for task_id in registered_task_ids:
        if task_id not in cron_manager_settings.CRONTAB_TASKS:
            CronTask.objects.get(id=task_id).delete()

    # Then, register any new ones.
    for task_name, task_func in cron_manager_settings.
