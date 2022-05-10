import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import stratum_listener
from . import util


class StratumClient(object):
    def __init__(self, host, port, username, password,
                 on_connect=None, on_disconnect=None, on_job=None,
                 on_solution=None, on_block=None, on_submit=None,
                 on_set_difficulty=None, on_log=None, on_difficulty=None,
                 on_submit_share=None, on_submit_block=None,
                 on_submit_upstream_block=None, on_error=None,
                 on_unknown_message=None, on_get_transactions=None,
                 on_get_block_template=None, on_submit_header=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.on_connect = on_connect
        self.on_
