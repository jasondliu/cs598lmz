import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# function that gets the initial value
def read_int():
    return int(sys.stdin.readline().strip())

read_ints = lambda: map(int, sys.stdin.readline().strip().split(' '))
read_int64s = lambda: map(int64, sys.stdin.readline().strip().split(' '))

def solve(n, a, b):
    if a[0] != 0:
        return 'IMPOSSIBLE'
    for i in xrange(n):
        if a[i] < b[i]:
            return 'IMPOSSIBLE'
        if i:
            if a[i] > a[i-1]+1:
                return 'IMPOSSIBLE'
            if b[i] < b[i-1]:
                return 'IMPOSSIBLE'
    return 'POSSIBLE'

for case in xrange(read_int()):
    n = read_int()

