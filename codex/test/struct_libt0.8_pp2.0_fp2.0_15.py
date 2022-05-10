import _struct
import boto
import cStringIO
import logging
import os
import re
import socket
import sys
import time
import timestamp
import pubsub

# Get the pubsub implementation that we want to use.
# If user has pubsub, use it.
pubsub = pubsub.load_pubsub()

# Size of the chunks to read from the file.
CHUNK_SIZE = 256 * 1024

if sys.version_info >= (3,):
    def bchr(x):
        return bytes([x])
else:
    bchr = chr

_test_fakes3_ok = False

try:
    _fakes3_import_ok = True
    import fakes3.request
except ImportError:
    _fakes3_import_ok = False

def fakes3_set_import_ok(ok=False):
    """Set the flag controlling whether we can write to a local
    fakes3 server.
    """
    global _fakes3_import_ok
    _fakes3_import_ok = ok

