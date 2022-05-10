import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p


@numba.jitclass([('x', types.voidptr)])
class J(object):
    def __init__(self):
        self.x = None

def loop(n):
    for i in range(n):
        x = S()
        x.x = i
        yield x.x

def loop_j(n):
    for i in range(n):
        x = J()
        x.x = i
        yield x.x

loop1 = numba.generated_jit(nopython=True)(loop)
loop2 = numba.generated_jit(nopython=True)(loop_j)

def check():
    data = list(loop(10))
    data1 = list(loop1(10))
    data2 = list(loop_j(10))
    data3 = list(loop2(10))
    print(data)
    assert data == data1 == data2 == data3

def main():
    loop1(10)
    loop2(10)


if
