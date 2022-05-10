import ctypes
import ctypes.util
import threading
import sqlite3
import time
import json
import os
import os.path
import struct
import traceback
import socket
import sys
import select
import fcntl
import errno

# TODO:
# - Add a way to set the default database file to use (currently hardcoded to ~/.local/share/dns-over-https/dns.db)
# - Add a way to set the default server to use (currently hardcoded to 1.1.1.1)
# - Add a way to set the default port to use (currently hardcoded to 853)
# - Add a way to set the default timeout (currently hardcoded to 10 seconds)
# - Add a way to set the default number of retries (currently hardcoded to 3)
# - Add a way to set the default edns0 size (currently hardcoded to 4096)
# - Add a way to set the default dnssec (currently hardcoded to True)
# - Add a way to set the default ndots (currently hardcoded to 1)
# - Add a way to set the default search domains (currently hardcoded to empty)
# - Add a way
