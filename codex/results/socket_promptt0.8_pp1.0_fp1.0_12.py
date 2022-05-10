import socket
# Test socket.if_indextoname()

import sys
import errno
import socket

from test_support import run_unittest, TestFailed, findfile

if_indextoname_src = """
#include <ifaddrs.h>
#include <net/if.h>

#ifndef ERANGE
#define ERANGE 34
#endif

const char *
if_indextoname(unsigned int index, char *ifname)
{
    return if_indextoname_generic(index, ifname);
}
"""
test_support.compile_helper(if_indextoname_src, 'test_if_indextoname', headers=['ifaddrs.h'])

class GetIfNameTests(unittest.TestCase):

    def test_get_if_name(self):
        f = open(findfile("ifnames"))
        for line in f:
            if line.startswith("if_nametoindex"):
                funcname, index, name = line.split()
                index = int(index)
                n = socket
