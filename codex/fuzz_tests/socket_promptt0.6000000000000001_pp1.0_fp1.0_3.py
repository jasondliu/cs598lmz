import socket
# Test socket.if_indextoname()
#
# This test checks if the function can handle invalid arguments
#
# Author: Alexander Zimmermann <alexander@azimmermann.com>
# Copyright: (c) 2013 Alexander Zimmermann <alexander@azimmermann.com>
# License: GPLv2

import sys
import socket

# Values for the socket family
AF_UNSPEC = 0
AF_UNIX = 1
AF_INET = 2
AF_INET6 = 10


def check_if_indextoname(log, family):
    """Run socket.if_indextoname() with invalid arguments."""

    if_index = -1

    # Invalid index
    try:
        socket.if_indextoname(family, if_index)
    except socket.error as error:
        err = error.args[0]

        if err == 'invalid argument':
            log.info('socket.if_indextoname() returned expected error: %s',
                     error)
        else:
            log.error('socket.if_indextoname() returned unexpected error: %
