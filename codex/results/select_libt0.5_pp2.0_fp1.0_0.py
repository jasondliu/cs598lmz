import selectors
import subprocess
import sys
import threading
import time
import traceback

from . import server
from . import util

# Use the system PRNG to select the seed.
random = random.SystemRandom()

# The default port number to use.
DEFAULT_PORT = 9999

# The default host to use.
DEFAULT_HOST = "localhost"

# The default number of threads to use.
DEFAULT_THREADS = 8

# The default number of clients to use.
DEFAULT_CLIENTS = 10

# The default number of requests to make.
DEFAULT_REQUESTS = 1000

# The default number of seconds to run for.
DEFAULT_RUN_SECONDS = None

# The default number of requests to make per second.
DEFAULT_REQUESTS_PER_SECOND = None

# The default number of requests to make per second.
DEFAULT_REQUESTS_PER_CLIENT = None

# The default number of requests to make per second.
DEFAULT_REQUESTS_PER_THREAD
