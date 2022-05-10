from types import FunctionType
a = (x for x in [1])
type(a)

type(a.next)

type(a.next())
type(a.next) == FunctionType
# generator can't be unpacked:
a1 = a.next
a1()
# generator can't be unpacked:
a1 = a.__iter__()
a1
a1.__iter__
a1.next
# generator is an iterator
# iterators are containers
a = a.__iter__()
a

a = a.next()
a

a = a.next()
a

try:
    a = a.next()
except:
    print "stop iterating"
# iterators are containers
a = (x for x in [1])
a

a = a.next()
a

# iterators are containers
a = (x for x in [1, 2, 3])
a

a = a.next()
a

a = a.next()
a

a = a.next()
a

try:
    a = a.next()
except:
    print "stop iter
