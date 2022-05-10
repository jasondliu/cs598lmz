import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os.path
import json
import sys

libc_path = ctypes.util.find_library('c')
libc = ctypes.CDLL(libc_path)

def get_thread_by_id(thread_id):
  return libc.dlmalloc_get_thread_by_id(ctypes.c_uint(thread_id))

def get_thread_id(thread):
  return libc.dlmalloc_get_thread_id(ctypes.c_void_p(thread))

def main():
  db = sqlite3.connect('ns-3_times.db')
  db.execute('CREATE TABLE IF NOT EXISTS times (id INTEGER PRIMARY KEY, t INTEGER, userReal INTEGER, systemReal INTEGER, userCpu INTEGER, systemCpu INTEGER)')

  # Initialize the times database
  thread = get_thread_by_id(0)
  db.execute('INSERT INTO times (t, userReal, systemReal, userCpu, system
