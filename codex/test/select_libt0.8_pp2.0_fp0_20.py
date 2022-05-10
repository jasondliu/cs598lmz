import select
import sys
import time
import errno

from ubnt.args import parser, Receiver_args, Sender_args, init_args
from ubnt.common import setup_logging, setup_ipc
from ubnt.ipc import open_ipc
from ubnt.sys import setup_sys, check_sys


class Sender:
    """
    Implementation of packet sender to eth1 interface
    """

    def __init__(self, args, log):
        self.args = args
        self.log = log
        self._pid = None
        self._stop = False

    def _sender_loop(self):
        """
        Main loop of sender process
        """
