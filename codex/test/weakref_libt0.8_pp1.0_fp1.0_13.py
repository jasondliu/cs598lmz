import weakref

import sys
import threading
import time
import traceback

import logging
_logger = logging.getLogger(__name__)
del logging

from .util import strtype, MIN_GRP_ID


# noinspection PyBroadException
def _watcher_thread(watcher):
    """
    BG thread to monitor a watcher
    :param watcher:
    :return:
    """
    last_time = watcher._last_run_time = time.time()
    while watcher.running:
        try:
            now = time.time()
            delta_t = now - last_time
            last_time = now
            watcher.tick(delta_t)
        except Exception:
            _logger.error("Exception in watched object", exc_info=True)
            pass
        finally:
            time.sleep(watcher.interval)


class Watcher(object):
    """
    Watches a list of watched objects and calls their tick() periodically
    """
