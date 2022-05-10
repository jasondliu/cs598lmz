from types import FunctionType
list(FunctionType(lambda x:x*x, [], {}).__code__.co_varnames)

import sys
sys.path.append('/Users/david/Documents/Python/')
import mymath
mymath.mypi.__code__.co_varnames

# The bytecode for a function object is stored in its __code__ attribute.
# The bytecode for a function is a sequence of instructions.
# Each instruction has a unique number, called the opcode.
# The opcode is the leftmost 8 bits of the instruction.
# The next 8 bits are used to store the instruction argument.
# The remaining 48 bits are unused.
# The opcode can be one of the following:
# Opcode			Argument			Meaning
# POP_TOP								Pops the top item off the stack
# ROT_TWO								Swaps the two top items of the stack
# ROT_THREE								Rotates the three top items of the stack to the left
# DUP_TOP				
