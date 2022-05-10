import gc, weakref
import logging
import os
import sys
import time
import traceback

from . import _util
from ._util import (
    _is_main_thread,
    _is_main_process,
    _is_main_greenlet,
    _is_main_coroutine,
    _is_main_task,
    _is_main_asyncio_loop,
    _is_main_thread_loop,
    _is_main_thread_greenlet,
    _is_main_thread_coroutine,
    _is_main_thread_task,
    _is_main_thread_asyncio_loop,
    _is_main_thread_asyncio_coroutine,
    _is_main_thread_asyncio_task,
    _is_main_thread_asyncio_future,
    _is_main_thread_asyncio_wait,
    _is_main_thread_asyncio_shield,
    _is_main_thread_asyncio_future_shield,
    _is_main_thread_asyncio
