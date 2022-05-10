import selectors
import socket
import types

from . import __version__
from . import config
from . import exceptions
from . import log
from . import utils
from . import web
from . import web_urllib
from . import web_requests


logger = logging.getLogger(__name__)


class Server:
    """
    An HTTP server that serves the current directory.
    """

    def __init__(self, host, port, daemon=False, quiet=False,
                 index=None, web_client=None, web_client_kwargs=None,
                 web_client_timeout=None, web_client_max_size=None,
                 web_client_max_redirects=None, web_client_max_retries=None,
                 web_client_verify_ssl=None, web_client_user_agent=None,
                 web_client_auth=None, web_client_proxies=None,
                 web_client_cert=None, web_client_timeout_download=None,
                 web_client_timeout_connect=
