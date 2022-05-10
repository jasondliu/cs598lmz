from types import FunctionType
list(FunctionType(code, globals=globals(), name='name', argdefs=(), closure=None))
"""

"""
from types import FrameType
list(FrameType(code, globals={}, locals={}, prev=None))
"""

"""
from types import CodeType
list(CodeType(argcount, kwonlyargcount, nlocals, stacksize, flags, code, consts, names, varnames, filename, name, firstlineno, lnotab, freevars, cellvars))
"""
