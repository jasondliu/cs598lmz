import gc, weakref

class Foo(object):
    pass

def bar():
    pass

def main():
    f = Foo()
    f.bar = bar
    f.bar()
    wr = weakref.ref(f)
    del f
    gc.collect()
    print wr()

main()
