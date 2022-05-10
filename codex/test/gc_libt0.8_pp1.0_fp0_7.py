import gc, weakref

def callback(reference):
    print('collected', reference)

