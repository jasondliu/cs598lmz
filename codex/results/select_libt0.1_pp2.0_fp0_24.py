import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import util
from . import version

# TODO:
# - Add a way to send a message to all clients
# - Add a way to send a message to all clients except one
# - Add a way to send a message to a specific client
# - Add a way to send a message to a specific client and all clients after it
# - Add a way to send a message to a specific client and all clients before it
# - Add a way to send a message to a specific client and all clients before and after it
# - Add a way to send a message to a specific client and all clients between two other clients
# - Add a way to send a message to a specific client and all clients between two other clients and all clients before and after it
# - Add a way to send a message to a specific client and all clients between two other clients and all clients before and after it and all clients before and after the two other clients
# - Add a way to send a message to a specific client and all clients between two other clients and all clients before and after
