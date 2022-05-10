from types import FunctionType
list(FunctionType(FunctionType(lambda:0,globals(),'f'),globals(),'g')())

# code objects
import dis
def f(): pass
dis.dis(f.__code__)

# bytecode
import marshal
marshal.loads(f.__code__.co_code)

# bytecode instructions
import opcode
opcode.opname[opcode.opmap['LOAD_GLOBAL']]

# bytecode optimization
def g():
    i = 1
    j = 2
    return i + j
dis.dis(g.__code__)
def h():
    return 1 + 2
dis.dis(h.__code__)

# bytecode interpreter
import sys
def f(x):
    return x + 1
def g(x):
    return x + 2
def h(x):
    return x + 3
def run(code):
    code = code.replace('\t', ' ' * 8)
    code = code.split('\n')
    code = [line.strip() for line in code]
    code
