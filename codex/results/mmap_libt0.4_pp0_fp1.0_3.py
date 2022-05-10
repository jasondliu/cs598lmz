import mmap
import os
import re
import sys
import time

from . import common
from . import config
from . import log
from . import utils
from . import version
from . import worker
from . import x11
from . import xcbq


def _init_logging():
    log.init(config.args.log_file)
    log.info('qutebrowser v{}'.format(version.version()))
    log.info('Command line: {}'.format(' '.join(sys.argv)))
    log.info('Config: {}'.format(config.instance.filename()))
    log.info('Config (yaml): {}'.format(config.instance.yaml_config_filename()))
    log.info('Config (autoconfig): {}'.format(config.instance.autoconfig_yaml()))
    log.info('Config (py): {}'.format(config.instance.py_config_filename()))
    log.info('Config (py) (autoconfig): {}'.format(
        config.instance.autoconfig_py()))
    log
