import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import fcntl
import os
from collections import defaultdict
import time
import traceback
from . import common, jumptable, utils
from . import config, logger

logger = logger.logger_for_me(__file__)


class Scale(object):

  def __init__(self, scale_name, scale_min, scale_maj):
    self.scale_name = scale_name
    self.scale_min = scale_min
    self.scale_maj = scale_maj

  def __repr__(self):
    return "<Scale {} {} {}>".format(self.scale_name, self.scale_min, self.scale_maj)


def get_offset(addr):
  offset = None
  if addr:
    if addr.startswith("offset="):
      offset = int(addr[7:])
  return offset


def get_offset_and_size(addr_size):
  offset = None
  size = None
  if addr_size:
    if addr_size.startswith("
