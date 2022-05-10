import mmap
import os
import sys
import time

from . import util
from . import version
from . import worker
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_aio_ctx = None


def get_aio_ctx():
    global _g_aio_ctx
    if _g_aio_ctx is None:
        _g_aio_ctx = libaio.io_setup(128)
    return _g_aio_ctx


class AioReadWorker(worker.Worker):
    def __init__(self, name, queue_size, aio_ctx, file_path, offset, data_len, read_callback):
        super(AioReadWorker, self).__init__(name, queue_size)
        self._aio_ctx = aio_ctx
        self._file_path = file_path
        self._offset = offset
        self._data_len = data_len
        self._read_callback = read_callback
        self._read_data =
