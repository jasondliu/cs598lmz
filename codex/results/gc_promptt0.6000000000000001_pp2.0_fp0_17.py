import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a finalizer.
def finalize(arg):
    print('finalizing', arg)

def make_finalizer():
    x = []
    x.append(x)
    wr = weakref.ref(x, finalize, 'x')
    del x
    return wr

def main():
    wr = make_finalizer()
    print(gc.collect(), 'unreachable objects')
    print(gc.collect(), 'unreachable objects')
    print(gc.collect(), 'unreachable objects')
    print(gc.collect(), 'unreachable objects')
    print(gc.collect(), 'unreachable objects')

if __name__ == '__main__':
    main()
