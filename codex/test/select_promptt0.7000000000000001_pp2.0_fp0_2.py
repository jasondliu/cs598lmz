import select
# Test select.select and select.poll
import signal
# Test signal.alarm and signal.signal
import socket
# Test socket.socket with timeout
import subprocess
# Test subprocess.Popen, .communicate and .wait
import sys
# Test sys.exit
import threading
# Test threading.Thread
import time
# Test time.sleep
import unittest
# Test unittest.TestCase.skipTest
import zmq
# Test zmq.Context.instance, zmq.Context.term and zmq.Socket

from twisted.trial.unittest import TestCase

from vumi.tests.utils import LogCatcher


def get_current_stack():
    return traceback.extract_stack()


def get_current_stack_frames():
    return [frame[2] for frame in get_current_stack()]


def get_current_stack_frame_names():
    return [frame[2] for frame in get_current_stack() if frame[2] != '<module>']


