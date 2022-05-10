import weakref

import aiohttp
import async_timeout

from . import error
from .query import Query
from .utils import cached_property
from .utils.async_utils import bound_coroutine
from .utils.iterable import build_dict_iterable
from .utils.iterable import build_model_iterable

__all__ = ['Session']


class Session:
    """
    A wrapper around an aiohttp.ClientSession with some convenience methods.
    """

    def __init__(self, api_key, api_secret=None, base_url='https://api.smartystreets.com',
                 client_session=None, api_version=None, batch_size=None,
                 max_coro_tries=3, retry_delay=1):
        """
        Args:
            api_key (str):
                The API key to be passed to the server.
            api_secret (str):
                The API secret to be passed to the server.
            base_url (str):
                The base URL for the API endpoints.
            client_session
