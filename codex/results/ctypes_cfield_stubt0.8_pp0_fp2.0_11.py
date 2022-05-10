import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

class B(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

ai = id(A())
bi = id(B())

# the following call takes about 800-1000 us
t0 = time.time()
x = id(A)
d = dict((k, v) for k, v in globals().items()
         if v is not x and id(v) == ai)
t = time.time() - t0
print('A: d = {}'.format(len(d)))

# the following call takes about 100 us
t0 = time.time()
x = id(A)
d = dict((k, v) for k, v in globals().items()
         if v is not x and id(v) == bi)
tt = time.time() - t0
print('B: d = {}'.format
