import select
import signal
import subprocess
import sys
import time
import traceback

from . import (
    config,
    constants,
    errors,
    jsonrpc,
    protocol,
    rpc,
    util,
)

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Testnet(object):
    """
    A bitcoin testnet instance.
    """

    def __init__(self, bitcoind_path, rpc_port, p2p_port, data_dir,
                 bitcoind_args=None, bitcoind_config=None, bitcoind_connect_args=None):
        self.bitcoind_path = bitcoind_path
        self.rpc_port = rpc_port
        self.p2p_port = p2p_port
        self.data_dir = data_dir

        self.bitcoind_args = bitcoind_args
        self.bitcoind_config = bitcoind_config
        self
