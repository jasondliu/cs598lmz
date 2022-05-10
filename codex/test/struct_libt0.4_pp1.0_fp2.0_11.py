import _struct
import _thread
import _threading
import _time
import _tracemalloc
import _traceback
import _types
import _warnings
import _weakref
import _weakrefset

from _testcapi import *
from _testbuffer import *
from _testimportmultiple import *
from _testinternalcapi import *
from _testmultiphase import *
from _testpackage import *
from _testthread import *
from _testbuffer import *


# Disable the buffering of stdout and stderr
class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

import sys
sys.stdout = Unbuffered(sys.stdout)
