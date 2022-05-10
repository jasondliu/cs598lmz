import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
import sys

# from .misc import get_logger, config_logging
from .misc import get_logger, PYTHON_VERSION, load_class, iteritems
from .type_check import *

from . import compat
from . import file_utils

import numpy as np

if PYTHON_VERSION == 3:
    from imp import reload

# from .log_utils import logging_config
from .res import get_config_path, get_data_path
from .context import Context
from .context import get_context

# from . import arch


# def get_default_context(device_id=0):
#     config = get_config()
#     # config = {'device_id': 0}
#     # print(config)
#     return get_extension_context(device_id=config['device_id'],
#                                  print_log=config['print_log'])
#
#
#
