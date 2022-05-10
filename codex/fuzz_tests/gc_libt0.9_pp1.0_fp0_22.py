import gc, weakref

class C(object):
    def __init__(self):
        print("C")

    def __del__(self):
        print("D")

def func():
    print("func")

if __name__ == '__main__':
    c = C()
    callback = weakref.ref(c, func)

    del c
    #callback = None
    #print(callback)
    gc.collect()
