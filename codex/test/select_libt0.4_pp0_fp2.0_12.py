import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import util

# Globals
#
# The global log object
logger = log.getLogger(__name__)

# The global server object
server = None

# The global config object
config = config.Config()

# The global server socket
serverSocket = None

# The global list of client sockets
clientSockets = []

# The global list of client threads
clientThreads = []

# The global list of client threads
clientThreadsLock = threading.Lock()

# The global server thread
serverThread = None

# The global server thread
serverThreadLock = threading.Lock()

# The global server thread
serverThreadLock = threading.Lock()

# The global server thread
serverThreadLock = threading.Lock()

# The global server thread
serverThreadLock = threading.Lock()

# The global server thread
serverThreadLock = threading.Lock()

# The global server thread
