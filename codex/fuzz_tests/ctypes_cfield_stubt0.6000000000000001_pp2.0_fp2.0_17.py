import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(msg, got, expected):
    if got != expected:
        print('%s: got %r, expected %r' % (msg, got, expected))

s = S()

s.x = -42
test('s.x', s.x, -42)
test('s.x.value', s.x.value, -42)
s.x.value = 42
test('s.x', s.x, 42)
test('s.x.value', s.x.value, 42)

try:
    s.x.value = 'spam'
except TypeError:
    pass
test('s.x', s.x, 42)
test('s.x.value', s.x.value, 42)

try:
    s.x.value = -2**31
except OverflowError:
    pass
test('s.x', s.x, 42)
test('s.x.value', s.x.value, 42)

try:
    s.x.value = 2**31-1
except Overflow
