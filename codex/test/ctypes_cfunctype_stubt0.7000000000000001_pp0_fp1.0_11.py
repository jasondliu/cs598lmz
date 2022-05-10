import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

if __name__ == "__main__":
    import sys
    import gc
    def callback(arg):
        print("callback", arg)
        print("num:", len(gc.get_objects()))
        print("callback done")
        global myfunc
        del myfunc
        print("num:", len(gc.get_objects()))
    print("num:", len(gc.get_objects()))
    gc.callbacks.append(FUNTYPE(callback))
    gc.disable()
    print("num:", len(gc.get_objects()))
    myfunc = fun
    print("num:", len(gc.get_objects()))
    del fun
    print("num:", len(gc.get_objects()))
    sys.stdout.flush()
    gc.collect()
    print("num:", len(gc.get_objects()))
    sys.stdout.flush()
    del myfunc
    gc.collect()
    print("num:", len(gc.get_objects()))
   
