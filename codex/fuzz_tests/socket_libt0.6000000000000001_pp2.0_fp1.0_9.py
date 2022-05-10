import socket
import sys
import time
import traceback

from django.core import exceptions
from django.core.mail import mail_managers

from django_statsd.clients import statsd
from django_statsd.patches.logging import log_exception

from celery import conf
from celery.datastructures import ExceptionInfo
from celery.log import setup_logger
from celery.messaging import establish_connection
from celery.registry import tasks
from celery.result import EagerResult
from celery.utils import gen_unique_id


def send_error_emails(context):
    """Sends error emails for the given context.

    :param context: The context to send error emails for.

    """
    exc_info = context.get("exc_info")
    if exc_info:
        subject = "Celery error: %s" % (context.get("task_name") or
                                        "Unknown task")
        exc_type, exc_value, tb = exc_info
        message = "\n".join([subject
