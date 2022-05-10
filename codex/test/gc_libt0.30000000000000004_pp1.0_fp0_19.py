import gc, weakref

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

def show_all_objects():
    for obj in gc.get_objects():
        print(repr(obj))

def main():
    show_all_objects()
    print('Creating a Foo')
    f = Foo('a')
    show_all_objects()
    print('Creating a weakref')
    wr = weakref.ref(f)
    show_all_objects()
    print('Deleting Foo')
    del f
    show_all_objects()
    print('gc.collect()')
    gc.collect()
    show_all_objects()
    print('wr() is {!r}'.format(wr()))

if __name__ == '__main__':
    main()
