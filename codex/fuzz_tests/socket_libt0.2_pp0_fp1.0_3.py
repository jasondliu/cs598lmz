import socket
import sys
import time

from . import utils
from . import config
from . import exceptions

logger = logging.getLogger(__name__)

class Client(object):
    """
    A client for the OpenStack Nova API.

    :param string username: Username for authentication. (optional)
    :param string api_key: API key for authentication. (optional)
    :param string project_id: Project ID for project scoping. (optional)
    :param string auth_url: Authentication URL. (optional)
    :param string region_name: Name of a region to select when choosing an
                               endpoint. (optional)
    :param string endpoint_type: The endpoint type to use. (optional)
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    :param bool insecure: SSL certificate validation. (optional)
    :param bool log_http: Allow for HTTP logging. (optional)
    :param string ca_cert: SSL CA bundle file to use. (optional)
    :param integer retries: How many times idempot
