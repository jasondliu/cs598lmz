import ctypes
ctypes.cast(1.1, ctypes.c_int)

list(map(int, [1.1, 2.2, 3.3]))

# Numeric Types
int(1.1)

float(1)

complex(1, 2)

# Strings
s = 'abc'
print(s[1])
print(len(s))
print(s + 'def')
print(s.upper())

s = 'a\nb\tc'
print(s)
print(len(s))

'%s, eggs, and %s' % ('spam', 'SPAM!')

template = '{0}, eggs, and {1}'
template.format('spam', 'SPAM!')

template = '{}, eggs, and {}'
template.format('spam', 'SPAM!')

# Sequence Types
s = 'spam'
print(s[0], s[-2])
print(s[1:3], s[1:], s[:-1])
print(s[:], s[:0], s[
