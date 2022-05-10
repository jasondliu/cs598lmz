import socket
# Test socket.if_indextoname()
#
# The test case is to check if socket.if_indextoname() can get an interface
# name from a given interface index.
#
# This test case is to check if the interface name can be get from an interface
# index.

import os
from autotest.client import utils
from autotest.client.shared import error

def run_if_indextoname(test, params, env):
    """
    Test socket.if_indextoname()

    @param test: KVM test object.
    @param params: Dictionary with the test parameters.
    @param env: Dictionary with test environment.
    """
    if_index = params.get("if_index")
    if_name = params.get("if_name")

    ifname = socket.if_indextoname(int(if_index))
