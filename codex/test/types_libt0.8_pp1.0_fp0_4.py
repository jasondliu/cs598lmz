import types
types.TypeType

type(42) is type

type('str')

type('str') == str

type([]) == list

def f(): pass
type(f) == types.FunctionType

class C: pass
type(C) == type

class D(object): pass
type(D) == type

class E(D): pass
type(E) == type

type(E) == type(D)

c = C()

type(c)

type(c) == C

type(E())

class c: __metaclass__ = type

c.__class__ == type

type(c)

isinstance(c, type)

isinstance(c(), c)

