fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# . access to the underlying code
fn.__code__
# . code objects are immutable
fn.__code__.co_code = 'a'
# . code objects can only be accessed through a function
fn.__code__.co_code
# . the bytecode is a sequence of instructions
fn.__code__.co_code
# . each instruction is compiled to a byte
fn.__code__.co_code[0]
# . we can disassemble the bytecode
dis.dis(fn.__code__.co_code)
# . the bytecode is a sequence of instructions
# . each instruction is encoded as a single byte
# . the instruction set is a set of functions taking different parameters
# . the instuction set maps the byte/instruction to a function
# . the instruction set also provide a human-readable representation
dis.opmap
# . the instruction set is an attribute of the dis module
# . https://github.com/python/cpython/blob/master/Python/ceval.c
# . https://github.com/python/cpython/bl
