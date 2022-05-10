import _struct
import string
import sys
import time
import types
import xml.sax.saxutils

# Flush stdout after every print function
class Unbuffered:
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
sys.stdout=Unbuffered(sys.stdout)

# Global variables
__version__ = "1.0"
__author__ = "Ole Christian Weidner"
