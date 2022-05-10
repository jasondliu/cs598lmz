import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def adder(length_of_code, add_or_subt):
    arr = [None] * length_of_code
    acc = 0
    i = 0
    while i < length_of_code:
        nextval = fun()
        acc = (acc + nextval) * add_or_subt
        arr[i] = acc
        i += 1
    return arr


def minimal_time(length_of_code, p):
    t1 = timeit.timeit('adder(length_of_code, 1)', number=p,
                       setup='from __main__ import adder; length_of_code = 20;')
    t2 = timeit.timeit('adder(length_of_code, -1)', number=p,
                       setup='from __main__ import adder; length_of_code = 20;')
    return min(t1, t2)

length_of_code_list = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
