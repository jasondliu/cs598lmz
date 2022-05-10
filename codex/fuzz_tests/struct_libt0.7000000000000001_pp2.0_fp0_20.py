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
__doc__ = """
Taken from:

http://code.activestate.com/recipes/278844/

License:

Copyright (c) 2002, O'Reilly Media, Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this

