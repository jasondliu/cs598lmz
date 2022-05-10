import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    import os

    # We must bind the socket to a local port or it may not be possible to
    # send to it (depending on the platform and its firewall configuration).
    # This is because the socket may end up with an address for which there
    # is no route on the host.
    #
    # Use localhost (127.0.0.1) so that we can run the test even if there
    # is no network.
    #
    # Use port 0 so that the kernel will choose an arbitrary unused port
    # for us.
    #
    # Note that we can't use "localhost" as the host in the UDP socket
    # constructor, because that won't work without a proper DNS setup on
    # the host.
    #
    # Note that we can't use "localhost" as the host in the UDP socket
    # constructor, because that won't work without a proper DNS setup on
    # the host.
    #
    # Note that we can't use "localhost" as the host in the UDP
