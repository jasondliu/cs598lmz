import socket
import ssl
import yaml

from kubernetes import client
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
from openshift.dynamic import DynamicClient
from urllib3.exceptions import MaxRetryError
from urllib3.util import Retry

from . import options
from . import utils
from .exceptions import HandlerError
from .exceptions import HandlerTimeoutError
from .safe_yaml import safe_load_all


def create_retry_after_connection_error(logger=None, max_retries=3):
    """Retry decorator.

    It tries to run a function 'max_retries' times if it fails with
    ConnectionError.

    Args:
        logger: logger instance
        max_retries (int): allowed number of retries

    Returns:
        retry: decorator
    """
    logger = logger or logging.getLogger(__name__)

    def retry(func):
        """Retry wrapper.

        Args:
            func:
