gi = (i for i in ())
# Test gi.gi_code.co_filename

class C:
    x = (i for i in ())
# Test C.x.gi_code.co_filename

def f():
    return (i for i in ())
# Test f().gi_code.co_filename

def g():
    def h():
        return (i for i in ())
    return h
# Test g().gi_code.co_filename

def j(k):
    return (i for i in ())
# Test j(1).gi_code.co_filename

def m():
    def n(o):
        return (i for i in ())
    return n
# Test m()(1).gi_code.co_filename

def p():
    def q(r):
        def s():
            return (i for i in ())
        return s
    return q
# Test p()(1)()

def t():
    def u():
        def v(w):
            return (i for i in ())
        return v
    return u
# Test t()()(1)

def x():
