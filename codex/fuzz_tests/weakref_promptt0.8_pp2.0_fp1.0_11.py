import weakref
# Test weakref.ref

#>>> class A:
#...     def __init__(self, x):
#...         self.x = x
#...     def __repr__(self):
#...         return 'A(%r)' % self.x
#...
#>>> a = A(10)
#>>> id(a)                  # doctest: +ELLIPSIS
#140212835067944
#>>> r = weakref.ref(a)
#>>> r
#<weakref at ...; to 'A' at ...>
#>>> r()
#A(10)
#>>> r().x
#10
#>>> r().x = 11
#>>> r().x
#11
#>>> a.x
#11
#>>> r2 = weakref.ref(a)
#>>> r2() is r()
#True
#>>> r2 is r
#False
#>>> r() is a
#True
#>>> r2() is a
#True
#>>> def callback(r):
#...     print("dead", r)
#...
#>>> r2 = weakref
