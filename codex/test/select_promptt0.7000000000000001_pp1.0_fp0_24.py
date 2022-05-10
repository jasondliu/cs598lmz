import select
# Test select.select() in a non-blocking way
# select.select() documentation says that it does not work with pipes on Windows.
import socket
import subprocess
import sys
import time

import pty

import mitogen.core
import mitogen.master
import mitogen.parent
import mitogen.service
import mitogen.utils

import testlib


def test_pipe_throughput():
    # Start a receiver at the parent end of the pipe, and a sender in a child
    # process. Measure the total throughput.
    context = mitogen.core.Context(broker=mitogen.master.Broker(is_parent=True))
    parent_pipe, _ = mitogen.parent.Pipe(context, [context])
    sender, receiver = mitogen.utils.socketpair()
    proc = subprocess.Popen([
        sys.executable,
        __file__.replace('pyc', 'py'),
        'pipe_throughput_sender',
    ], stdin=sender)

    received = 0
