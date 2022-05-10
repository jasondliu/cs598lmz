from types import FunctionType
a = (x for x in [1])
print a

import gc

gc.set_debug(gc.DEBUG_LEAK)


def test():
    def root():
        for i in range(10000000):
            c = 1+1
    root()

test()

'''a = [1,2,3,4]
b = [1,2,3,4]
print id(a)
print id(b)'''
