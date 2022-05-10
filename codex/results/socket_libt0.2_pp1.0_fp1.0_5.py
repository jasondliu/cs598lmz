import socket
import sys
import threading
import time
import traceback

import pytest

from . import util
from .util import (
    assert_raises_rpc_error,
    connect_nodes,
    connect_nodes_bi,
    disconnect_nodes,
    get_datadir_path,
    initialize_chain_clean,
    p2p_port,
    wait_until,
)

# Test that the -alertnotify option triggers an alert.
# This test is not run by default. To run it, use the command:
# python3 -m test_framework.alertnotify_test

# 1. Start a node and generate 3 blocks
# 2. Set the -alertnotify script to a script that does nothing
# 3. Generate 2 more blocks
# 4. Verify that no alert was triggered
# 5. Set a new alert
# 6. Verify that the alert was triggered


class AlertTest(util.BitcoinTestFramework):
    def set_test_params(self):
        self.num_nodes = 1
        self.setup_clean
