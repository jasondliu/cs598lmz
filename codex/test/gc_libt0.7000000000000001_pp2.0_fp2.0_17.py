import gc, weakref

def on_finalize(ref):
    print('on_finalize: object is going to be destroyed')

