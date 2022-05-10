import socket
import threading
import json
import time
import pprint

# The port on which to listen
listenPort = 12000

# The port on which to send
sendPort = 12001

# The host to send to
sendHost = "localhost"

# The host to listen on
listenHost = "localhost"

# The lock for the file
lock = threading.Lock()

# The dictionary containing the file
file = {}

# The dictionary containing the file
file2 = {}

# The dictionary containing the file
file3 = {}

# The dictionary containing the file
file4 = {}

# The dictionary containing the file
file5 = {}

# The dictionary containing the file
file6 = {}

# The dictionary containing the file
file7 = {}

# The dictionary containing the file
file8 = {}

# The dictionary containing the file
file9 = {}

# The dictionary containing the file
file10 = {}

# The dictionary containing the file
file11 = {}

# The dictionary containing the file
file12 = {}

# The dictionary containing the file
