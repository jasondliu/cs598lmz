import socket
# Test socket.if_indextoname()
#
# This test checks that the function properly converts a network interface
# index to its name.
#
# Author: Satoru SATOH <ssato redhat.com>
# License: MIT
#
import os.path
import sys
import sos_analyzer.scanner.base
import sos_analyzer.scanner.ifconfig as TT

from sos_analyzer.tests.common import setup_workdir, cleanup_workdir


def test_10():
    """
    >>> iface_index = TT.if_indextoname(socket.AF_INET, 1)
    >>> assert iface_index == "lo"
    """
    pass


def test_20():
    """
    >>> iface_index = TT.if_indextoname(socket.AF_INET6, 1)
    >>> assert iface_index == "lo"
    """
    pass


def test_30():
    """
    >>> iface_index = TT.if_indextoname(socket.AF_INET, 2)
    >>> assert
