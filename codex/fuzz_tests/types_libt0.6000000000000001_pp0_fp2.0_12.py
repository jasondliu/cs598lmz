import types
types.new_class('A') # create a new class A
class A: pass # but A is still an old-style class

class B(object): pass # B is a new-style class
class C(A): pass # C is an old-style class
class D(B): pass # D is a new-style class

print type(A) # old-style class
print type(B) # new-style class
print type(C) # old-style class
print type(D) # new-style class

print A.__bases__ # old-style bases tuple
print B.__bases__ # new-style bases tuple
print C.__bases__ # old-style bases tuple
print D.__bases__ # new-style bases tuple

A.__bases__ += (B,) # illegal in new-style classes

print A.__bases__ # old-style bases tuple
print B.__bases__ # new-style bases tuple
print C.__bases__ # old-style bases tuple
print D.__bases__ # new-style bases tuple

class E
