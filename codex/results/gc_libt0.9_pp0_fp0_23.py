import gc, weakref, operator
from billiard import eintr_retry_call
from django.utils.log import getLogger
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, IntegrityError, connection, DatabaseError
from celery import current_task, task
from celery.signals import task_prerun
from celery.exceptions import RetryTaskError
from celery.utils.log import get_task_logger
from djcelery.models import TaskMeta
from . import api, models, progress, utils
from .exceptions import *
from .python import Python, PythonFinder, GnuplotFinder
from .lock import LockManager
from .registry import Registry
from .concurrency import Process, Pool


SUBTASK_TASK_ID_PATTERN = r'^\d+\w+@\w+\d$'  # e.g.: '10aad7ac
