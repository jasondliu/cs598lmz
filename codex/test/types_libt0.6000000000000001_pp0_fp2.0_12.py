import types
types.new_class('A') # create a new class A
class A: pass # but A is still an old-style class

class B(object): pass # B is a new-style class
class C(A): pass # C is an old-style class
class D(B): pass # D is a new-style class

