import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

def f(i):
    return view[i]

def g(i):
    return f(i)

def h(i):
    return g(i)

def j(i):
    return h(i)

def k(i):
    return j(i)

def l(i):
    return k(i)

def m(i):
    return l(i)

def n(i):
    return m(i)

def o(i):
    return n(i)

def p(i):
    return o(i)

def q(i):
    return p(i)

def r(i):
    return q(i)

def s(i):
    return r(i)

def t(i):
    return s(i)

def u(i):
    return t(i)

def v(i):
    return u(i)

def w(i):
    return v(i)

def x(i):
    return w(i)

def
