import socket
import sys
import threading
import time

# The port used for the server.
PORT = 8888

# The number of seconds to wait between each request.
REQUEST_DELAY = 0.1

# The number of seconds to wait between each request.
RESPONSE_DELAY = 0.1

# The maximum number of requests to send.
MAX_REQUESTS = 1000

# The number of requests to send before the client sends a reset.
RESET_REQUESTS = 10

# The maximum number of bytes to send in a request.
MAX_REQUEST_BYTES = 1024

# The maximum number of bytes to send in a response.
MAX_RESPONSE_BYTES = 1024

# The maximum number of bytes to send in a reset.
MAX_RESET_BYTES = 1024

# The number of bytes to send to the server.
NUM_BYTES = 1024

# The number of bytes to send to the server.
NUM_REQUESTS = 100

# The number of connections to make.
