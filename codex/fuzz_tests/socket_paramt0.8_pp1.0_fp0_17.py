import socket
socket.if_indextoname(2)
{'AF_INET', 'AF_INET6', 'AF_LINK'}.issubset(dir(socket)) # this works too

import sqlite3 as db
help(db.connect)
# or
dir(db.connect)

import subprocess
dir(subprocess)

import sys
'argv' in dir(sys)

print('\n'.join(dir(sys))) # to list all

import time
dir(time)

import types
dir(types)

import urllib
dir(urllib)
