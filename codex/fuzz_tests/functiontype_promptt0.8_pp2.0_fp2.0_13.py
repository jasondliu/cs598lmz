import types
# Test types.FunctionType
print isinstance(lambda x: x + 1, types.FunctionType), "lambda"
print isinstance(fact, types.FunctionType), "function"
print isinstance(zip, types.BuiltinFunctionType), "built-in function"
print isinstance(len, types.BuiltinFunctionType), "built-in method"
print isinstance([].append, types.MethodType), "method"
print isinstance(str.lower, types.MethodType), "built-in method"

import sys
print sys.getrecursionlimit()
import os
print os.environ["PATH"]
print os.popen("ls -l").readlines()
print os.getcwd()

# import
import sys, os
import math as calc
print calc.log(4)

# from
from math import sin, pi
print sin(pi / 2)
from math import *
print log(e)
from math import log as ln
print ln(e)

print "Say something: "
# input()

# print a,
# print "Good",

# format
print
