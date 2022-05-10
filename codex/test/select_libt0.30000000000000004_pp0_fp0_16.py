import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import util
from . import xlog

xlog.log_init()
logger = xlog.getLogger("gae_proxy")

current_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(current_path, os.pardir, os.pardir))
data_path = os.path.abspath(os.path.join(root_path, os.pardir, os.pardir, 'data'))

