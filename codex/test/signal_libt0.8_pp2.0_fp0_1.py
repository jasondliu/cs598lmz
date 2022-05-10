import signal
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

try:
    from gevent import monkey
    monkey.patch_all()
except ImportError:
    pass

import logging
from logging import DEBUG, INFO, ERROR
import os

from .util import get_log_fname
# from .config import defaults, config_file, CONFIG_DIR

logger = logging.getLogger(__name__)

def set_default_logger(log_fname=None):
    log_fname = get_log_fname()
    if not os.path.exists(log_fname):
        logger.info('Creating log file %s' % log_fname)
    # hlog is the handler to be added to the root logger
    hlog = logging.FileHandler(log_fname)
