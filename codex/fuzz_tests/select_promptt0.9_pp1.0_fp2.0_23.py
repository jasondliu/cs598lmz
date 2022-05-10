import select
# Test select.select

#--------------------------------------------------------------------------------

import socket

def select_udp_echo():
    # Normally this would be set to a reasonable maximum,
    # like 4096, but to illustrate the code we are submitting
    # to this test the buffer only holds a small number of bytes.
    buffer_size = 2
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 50000))
    # This must be non-blocking so that test code below has a
    # chance to check select results.
    server_socket.setblocking(0)

    while True:
        # Support rlist and elist
        rlist, elist, olist = select.select(
            [server_socket], [], [], 2.0)

        if elist:
            raise RuntimeError("Unexpected exception list: " + repr(elist))
        if olist:
            raise RuntimeError("Unexpected output exception list: " +
                               repr(elist))
        if rlist:
            client_address = None
            data
