import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time
import codecs
import mmap
import struct
import argparse
import os
import time

from multiprocessing import Process, Queue


#print("getVersion: " + str(lib.getVersion()))
#print("hello: " + lib.hello())
#print("hello_callBack: " + lib.hello_callBack())

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def get_uid():
  return ''.join(random.choice('0123456789ABCDEF') for i in range(16))

def hello():
  return "hello world"

def hello_call_back(callback):
  print("hello_call_back")
  callback("hello world")

def hello_call_back_2(callback):
  print("hello_call_back_2")
  callback("hello world_2")
