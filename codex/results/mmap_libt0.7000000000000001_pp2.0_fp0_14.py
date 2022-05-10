import mmap
import os
import sys
import subprocess
import signal

from pprint import pprint
from . import config
from . import log

# global reference to buffered input
input_buffer = None

# global reference to buffered output
output_buffer = None

# global reference to child process
child = None

# global reference to child pid
pid = None

# global reference to child stdin
stdin = None

# global reference to child stdout
stdout = None

# global reference to child stderr
stderr = None

def initialize():
    global input_buffer
    global output_buffer
    global child
    global pid
    global stdin
    global stdout
    global stderr

    # initialize input buffer
    input_buffer = RingBuffer(config.get('input_buffer_size'))

    # initialize output buffer
    output_buffer = RingBuffer(config.get('output_buffer_size'))

    # create command to connect to socket
    command = [
        config.get('lmp_path'),
        '-s', config.
