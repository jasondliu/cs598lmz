import gc, weakref

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

def show_all_objects():
    for obj in gc.get_objects():
        print(obj)

def main():
    show_all_objects()
    print('Creating a Foo')
    f = Foo('f')
    show_all_objects()
    print('Creating a weakref to a Foo')
    wref = weakref.ref(f)
    show_all_objects()
    print('Deleting Foo')
    del f
    show_all_objects()
    print('gc.collect()')
    gc.collect()
    show_all_objects()
    print('wref:', wref)
    print('wref():', wref())

if __name__ == '__main__':
    main()
