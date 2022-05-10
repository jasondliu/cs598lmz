import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

c_lib = ctypes.CDLL("./solution.so")
c_lib.solution.argtypes = (ctypes.c_int, ctypes.c_int, FUNTYPE)

@FUNTYPE
def py_count_change(amount, kinds_of_coins):
    return count_change(amount, kinds_of_coins)

c_lib.solution(10, 4, py_count_change)
 
# Question 3

def make_accumulator(n):
    def add(amount):
        nonlocal n
        n += amount
        return n
    return add

acc = make_accumulator(1)
print(acc(5))
print(acc(2))
