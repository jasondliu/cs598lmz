import ctypes
import ctypes.util
import threading
import sqlite3
import curses
import time
from subprocess import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO


class myThread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      #print "Starting " + self.name
      print_time(self.name, self.counter, 0)
      print "Exiting " + self.name

def print_time(threadName, delay, counter):
   print "Starting " + threadName
   lock.acquire()
   global krzys1
   krzys1=threadName
   time.sleep(counter)
   lock.release()
   print "Exiting " + threadName

def accread(libname, tblname, data):
  global cur
  cur=con.cursor()
  cur.execute("INSERT
