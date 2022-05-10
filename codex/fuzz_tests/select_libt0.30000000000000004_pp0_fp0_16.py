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

if __name__ == "__main__":
    import sys
    current_path = os.path.dirname(os.path.abspath(__file__))
    python_path = os.path.abspath( os.path.join(current_path, os.pardir, 'python27', '1.0'))

    noarch_lib = os.path.abspath( os.path.join(python
