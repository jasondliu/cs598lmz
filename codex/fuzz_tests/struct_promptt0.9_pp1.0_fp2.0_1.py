import _struct
# Test _struct.Struct.from_buffer()
assert(_struct.Struct.from_buffer('p', _buffer).format == 'p')
%%cython --cplus

import _struct
# Test _struct.Struct.from_buffer()
assert(_struct.Struct.from_buffer('i', b'1234').unpack() == (4660,))
%%cython --cplus
libcpp.new_intp.restype = int
libcpp.new_intp.arg_types = [int]

def f(int x):
    intp = libcpp.new_intp(x)
    return intp[0]

f
%%cython --cplus

cdef void f(char *p):
    print('f(%s)' % p)
    
def g(p):
    f(p)
    
g('super')
%%cython --cplus

cdef void f(char *p):
    print('f(%s)' % p)
    
def g(p):
    f(p)
    
g('super')
%%cy
