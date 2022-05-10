from lzma import LZMADecompressor
LZMADecompressor()

from functools import partial
from multiprocessing import (
    cpu_count,
    get_logger,
    get_reduction_op,
    Pool,
)
logger = get_logger()
from pickle import dumps
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterable,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
)


__all__ = ['multireduce']


S = TypeVar('S', covariant=True)
T = TypeVar('T')


class MultiprocessPool(Pool):

    def apply_async_Logger(self, func, args=(), kwds={}, *, callback=None):
        '''
        Apply the given function to all args in the iterable, and
        collect the results
        If a callback is provided, it is executed straightaway
        (ahead of the call to .join() in this function)
        :param func:

        '''

       
