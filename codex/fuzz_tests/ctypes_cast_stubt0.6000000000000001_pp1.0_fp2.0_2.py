import ctypes
ctypes.cast(f.__code__.co_consts[1], ctypes.py_object).value

# this is how we can find the names of the parameters
f.__code__.co_varnames

# to find out where the function is defined
f.__code__.co_filename
f.__code__.co_firstlineno

# we can also see the raw bytecode of the compiled function
f.__code__.co_code

# and we can use the dis module to disassemble the bytecode into mnemonics
import dis
dis.dis(f)

# we can also get the bytecode directly from the function
bytecode = f.__code__.co_code

# we can iterate over the bytecode
for i in f.__code__.co_code:
    print(i)

# we can also unpack the bytecode into mnemonics and arguments
import struct
unpacked_code = struct.unpack('B'*len(bytecode), bytecode)
for i in unpacked_code:
    print(i)


