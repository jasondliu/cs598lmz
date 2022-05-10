import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGTERM, signal.SIG_DFL)

import sys
import json
import subprocess
import base64
import time

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebChannel

from . import config

from . import log
logger = log.get_logger('core')


def get_version():
    try:
        code = subprocess.check_output([
            'git', 'describe', '--always',
            '--dirty'
        ]).decode('utf-8')
        return 'from git ' + code
    except Exception:
        import nnimgspider
        return nnimgspider.__version__

