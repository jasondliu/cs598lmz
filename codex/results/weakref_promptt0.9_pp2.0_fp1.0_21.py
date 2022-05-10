import weakref
# Test weakref.ref
c = Fraction()
d = Fraction()
f = weakref.ref(c)
print(f())
print(f() is c)
print(f() is d)
c = 2
print(f())

# print([Fraction().__class__.__name__ for _ in range(4000)])

# __slots__

# Avoid dynamic attribute creation if p
