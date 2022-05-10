import _struct
# Test _struct.Struct
import a
import struct
a.set_struct(struct.Struct("BB"))
struct.Struct("BB").__reduce_ex__(5) # this is what pypy does

# Test _struct.Struct's args are a tuple
a.set_struct(struct.Struct("BB", 1))

a.set_struct(struct.Struct(""))
a.set_struct(struct.Struct("5s5s", "hello", "world"))

a.throw_keyerror(struct.Struct("!c"))

# test default _format_
a.set_struct(struct.Struct("@20s", u"Hello\u1234"))

a.set_struct(struct.Struct("i"))
a.set_struct(struct.Struct("ll"))
a.set_struct(struct.Struct("dd"))

import array
def repr_long(n):
    if '%x' % n == '-1':
        return '-1L'
    else:
        return repr(n)

