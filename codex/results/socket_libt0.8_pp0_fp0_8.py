import socket
import sys
import threading
from threading import Thread
import time
import iot_pb2

class DeviceClient:
  def __init__(self, ip, port, device_id, debug=False):
    self.ip = ip
    self.port = port
    self.device_id = device_id
    self.debug = debug
    self.run_event = threading.Event()
    self.run_event.clear()
    self.socket_lock = threading.Lock()
    self.sock = None
    self.connect_cb = None
    self.failure_cb = None
    self.send_cb = None
    self.receive_cb = None
    self.socket_thread = Thread(target=self.socket_thread_func)
    self.socket_thread.daemon = True
    self.socket_thread.start()

  def connect(self, connect_cb, failure_cb, send_cb, receive_cb):
    try:
      self.connect_cb = connect_cb
      self.failure_cb = failure_
