import _struct
# Test _struct.Struct methods

import array
import sys
from test import support
from test.support import bigaddrspacetest

def roundtrip(struc, *data):
    for fn in 'pack unpack'.split():
        m = getattr(struc, fn)
        s = m(*data)
        d = m(s)
        if d != data:
            raise AssertionError('Roundtrip %s:%s %s != %s' % (struc.format, fn,
                d, data))

def bigaddrspacetest(fn):
    bigaddrspacetest()(fn)

@bigaddrspacetest
def test_struct_1():
    roundtrip(_struct.Struct('=b'), 123)
    roundtrip(_struct.Struct('=B'), 123)
    roundtrip(_struct.Struct('=B'), 0xffffff)

@bigaddrspacetest
def test_struct_2():
    roundtrip(_struct.Struct('=h'), 0)
    roundtrip(_struct.Struct('=h'), 0xffffffff)
