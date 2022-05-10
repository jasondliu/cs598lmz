import gc, weakref

class Object(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

    def __del__(self):
        print('%s.__del__()' % self)

def weakref_cb(obj_ref):
    print('weakref_cb(%s)' % obj_ref)

def test():
    o = Object('test')
    obj_ref = weakref.ref(o, weakref_cb)
    print('o:', o)
    print('obj_ref:', obj_ref)
    print('obj_ref():', obj_ref())
    print('o is obj_ref():', o is obj_ref())
    print('o == obj_ref():', o == obj_ref())

    del o
    gc.collect()
    print('obj_ref():', obj_ref())

if __name__ == '__main__':
    test
