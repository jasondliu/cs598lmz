import socket
import threading
import unittest

import httplib2
import mox

import gflags as flags

FLAGS = flags.FLAGS


class HttpServer(object):
  """A simple HTTP server in Python."""

  def __init__(self, port):
    self.httpd = None
    self.port = port
    self.thread = threading.Thread(target=self._StartServer)
    self.thread.setDaemon(True)
    self.thread.start()
    self._WaitForServerToStart()

