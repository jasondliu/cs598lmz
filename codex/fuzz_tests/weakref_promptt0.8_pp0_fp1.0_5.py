import weakref
# Test weakref.ref(obj, _remove)
class Foo:
    def __init__(self):
        self.x = 0
    def __del__(self):
        print('deleting foo')
        self.x = 42
    def inc(self):
        self.x += 1

alist = []
def remove(wr):
    obj = wr()
    if obj is not None:
        print('object {0} still exists, but will be removed from'
              ' the list'.format(obj))
        alist.remove(wr)
    else:
        print('object does not exist anymore')

for i in range(10):
    obj = Foo()
    obj.inc()
    ref = weakref.ref(obj, remove)
    alist.append(ref)
    print('ref count = {0}'.format(sys.getrefcount(obj)))

clear_refs = list(alist)
while clear_refs:
    ref = clear_refs.pop()
    obj = ref()
    if obj is not None:
        obj.inc()
       
