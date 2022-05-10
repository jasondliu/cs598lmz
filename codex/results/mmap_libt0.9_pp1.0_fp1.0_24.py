import mmap
import os
import re
import sys

class MapDataset(object):
  def __init__(self, filename):
    self.filename = filename
    self.mm = None
    self.pos = 0
    statinfo = os.stat(self.filename)
    self.size = statinfo.st_size

  def __enter__(self):
    self.mm = open(self.filename, "r+b")
    self.mm = mmap.mmap(self.mm.fileno(), 0)
    self.pos = 0
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    self.mm.close()

  def readuntil(self, delim, use_current=True):
    if use_current:
      pos = self.pos
    else:
      pos = 0
    self.mm.seek(pos)
    chunk = self.mm.readline()
    if not chunk: return ""
    if chunk.endswith(delim):
      if not use_current: self.pos = 0
