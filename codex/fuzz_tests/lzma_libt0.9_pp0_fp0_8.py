import lzma
lzma.LZMACompressor()
import bz2
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import starmap,islice
import operator
from heapq import nlargest
from timeit import timeit
#   os.chdir("/home/wushang/Documents/Python")
class Vector(object):
    #   http://stackoverflow.com/questions/13373611/python-how-to-dynamically-add-new-method-to-an-instance
        #   https://docs.python.org/2/reference/datamodel.html
    def __init__(self,*args):
        self.args=args
    def __str__(self):
        return "<<" + ",".join (str(x) for x in self.args) + ">>"
    def __add__(self,other) :
        if len(self.args) != len(other.args) :
            raise TypeError("dimension mismatch")
        return Vector(*tuple(x+y for x,y
