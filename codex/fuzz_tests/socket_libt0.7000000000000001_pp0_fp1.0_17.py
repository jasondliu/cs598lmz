import socket
import struct
import time

# This is the port which the JTAG daemon uses to communicate with the
# server.
JTAG_PORT = 4444

# This is the port which the server uses to communicate with the JTAG
# daemon.
SERVER_PORT = 4445

# This is the size of the buffer we use to receive data from the JTAG
# daemon.
BUFFER_SIZE = 1024

# This is the template for the request to the JTAG daemon. It includes
# the command, the number of bits, the device number, the data to be
# written, and the offset into the device.
REQUEST_TEMPLATE = "<B B B %s B"

# This is the template for the response from the JTAG daemon.
RESPONSE_TEMPLATE = "<B B %s"

# This is the list of commands for the JTAG daemon.
COMMAND_CODES = {
    'read': 0,
    'write': 1,
    'reset': 2,
}

# These are the error codes returned by the JTAG daemon.

