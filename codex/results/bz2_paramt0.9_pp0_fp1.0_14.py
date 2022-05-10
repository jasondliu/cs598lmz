from bz2 import BZ2Decompressor
BZ2Decompressor()
#print(BZ2Decompressor())

# bytes
s= 'hello'
s[0]
#s.decode('utf') error
#s.encode('utf') error
#str.encode(s,'utf')

# iterable
l=[1,2,3]
i=iter(l)
next(i)
next(i)
next(i)
next(i)
next(i)
next(i)

# iterator
import re
i=iter(re.match('(b3)','b3abc'))
next(i)
next(i)

# function
def plus(x):
    return x+1
plus.__name__
plus.__doc__
plus.__module__

# not function
i=iter([1,2,3])
#i.__name__
#i.__doc__
#i.__module__

# type
type(plus)
plus.__class__
type(i)
i.__class__

# class
class MyIterable:
    def __
