fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can compile the same code object multiple times.
fn.__code__ = fn.__code__
fn()

# Test that we can compile code objects that are allocated by a
# different interpreter (but have the same address size, endianness,
# and alignment).
import struct
if struct.calcsize("P") == 8:
    c = compile("pass", "?", "exec", dont_inherit=True)
    fn.__code__ = c
else:
    c = compile("pass", "?", "exec", dont_inherit=True)
    fn.__code__ = c
fn()

# Test that we can compile code objects that are allocated by a
# different interpreter (with a different address size).
if struct.calcsize("P") == 8:
    c = compile("#".encode("ascii")*10000, "?", "exec", dont_inherit=True)
else:
    c = compile("#".encode("ascii")*10000, "?", "exec", dont_inherit=
