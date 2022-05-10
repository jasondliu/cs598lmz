import select
# Test select.select against poll

import select
import socket
import time
import threading

class MyPoll:
  def __init__(self, timeout = 0.0):
    self.timeout = timeout
    self.active  = False
    self.timeout_time = 0.0
    self.fdmap    = {}
    self.poll_obj = select.poll()
  def register(self, fd, event):
    self.poll_obj.register(fd, event)
    self.fdmap[fd] = event
  def modify(self, fd, event):
    if self.fdmap[fd]:
      self.fdmap[fd] = event
      self.poll_obj.modify(fd, event)
  def poll(self, timeout=None):
    t = self.timeout
    if timeout is not None: t = timeout
    if t == 0.0 and self.active:
      t = None
    if t is not None:
      if self.timeout_time and self.timeout_time < time.time():
        return [], [], []
