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

