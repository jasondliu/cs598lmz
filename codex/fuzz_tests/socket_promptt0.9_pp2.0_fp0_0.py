import socket
# Test socket.if_indextoname function basic
#
# 
# Tested function:
#       if_indextoname()
#

import os
import uuid
import socket
import array
from random import randint

from random import shuffle

import struct
import fcntl

import func_tests

lo_ifnum = 0

def test_if_indextoname(logFd):

    for i in range(randint(1, (1 << 32) - 1)):

        try:
            ifname = socket.if_indextoname(i)
            print("RECV: %s" % (ifname))

        except:
            continue

        if i == lo_ifnum:
            if ifname != "lo":
                return 1

            return 0

    return 1

if __name__ == "__main__":
    func_tests.run_test(test_if_indextoname)
