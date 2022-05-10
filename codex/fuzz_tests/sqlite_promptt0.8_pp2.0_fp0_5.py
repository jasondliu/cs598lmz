import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:temp?mode=memory&cache=shared')
import time
import os
import dropbox
import socket
import sys
import shutil
import math
import struct

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from node_api import *

### Globals ###

# these are used to keep track of nodes generating and receiving traffic from other nodes on the network
nodes = {}

# settings for local sqlite3 database; this is used for testing only and can probably be removed
sqlite3_db = sqlite3.connect('file:temp?mode=memory&cache=shared')
sqlite3_cursor = sqlite3_db.cursor()

# settings for access to network (via dropbox)
# this can be removed and replaced with whatever networking library you want to use
dropbox_token = 'H6GwE5Nn0DAAAAAAAAAAH5CNWGQ2aNvCcNUpz8eGTFRCpCzwaHv6UiJW8ly9mR
