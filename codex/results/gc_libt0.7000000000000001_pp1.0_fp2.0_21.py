import gc, weakref

class Test:
    def __init__(self):
        print('__init__()')

    def __del__(self):
        print('__del__()')


def weak_instance():
    t = Test()
    print(id(t))
    print(gc.get_referents(t))

    r = weakref.ref(t)
    print(r)
    print(r())

    print(gc.get_referents(t))

    t = None
    print(r())
    print(gc.get_referents(t))
    print(gc.collect())
    print(r())

    print(gc.get_referents(t))


if __name__ == '__main__':
    weak_instance()
