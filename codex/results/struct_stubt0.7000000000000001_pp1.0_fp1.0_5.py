from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.pack(-1)

import _struct
import struct

_struct.pack('<h', -1)
struct.pack('<h', -1)


"""
I saw this while running the testsuite

I haven't seen this in a while, but it used to be fairly common

I have no idea why it happens

The problem is that the file is compiled before the module that it
imports is compiled, and so the file does not know about the types
of the objects it is trying to use.  The compiler really should
compile the file in two passes.  The first pass would use a
slightly simpler grammar to compile the file, and would use
placeholders for the objects that don't yet exist.  The second pass
would then use the real grammar to compile the file using the objects
that were created in the first pass.  The placeholders should be
created using weakrefs, so that if the object doesn't exist, the
placeholder goes away.

I have an example of this, but I can't find it right now.  I'll
post
