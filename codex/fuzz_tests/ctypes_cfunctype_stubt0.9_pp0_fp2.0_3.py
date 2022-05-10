import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def f():
    x = 10
    return x
lfun = LOADER.get_function(fun)
lfun()
 

f1 = LOADER.get_function(f)
f1()

CODESTORE.debug_info
 

CODESTORE.dump_extract()
CODESTORE.extract()

CODESTORE.abstract_ops()


def pentier(n):
    cnt = 0
    i = 0
    j = 1
    k = 2
    l = 3
    m = 4
    while cnt < n:
        i = j
        j = k
        k = l
        l = m
        m = i + j + k + l + m
        cnt += 1
        yield m

p = pentier(100)
next(p)
CODESTORE.dump_extract()

def sum_k():
    s = 0
    while True:
        n = yield
        s += n
        yield s

sk = sum_
