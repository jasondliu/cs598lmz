from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# Slicing
a = [1, 2, 3]
a[1:]
a[1:2]
a[-2:]
a[:-2]

b = a[1:]
b[0] = 5
a

# Strings
'x' * 10
'hello'.upper()
'hello, world'.title()

a = 'hello'
b = 'world'
a + b

# Case-insensitive string comparisons
'a' == 'A'
'a'.upper() == 'A'

# String formatting
'%s, eggs, and %s' % ('spam', 'SPAM!')
'{0}, eggs, and {1}'.format('spam', 'SPAM!')

# String formatting, alternative
'{}, eggs, and {}'.format('spam', 'SPAM!')
'{0}, eggs, and {1}'.format('spam', 'SPAM!')
'{1}, eggs, and {0}'.format('spam', 'SPAM
