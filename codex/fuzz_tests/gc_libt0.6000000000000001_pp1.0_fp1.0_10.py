import gc, weakref

class A(object):
    def __del__(self):
        print 'deleted'

def func():
    a = A()
    ref = weakref.ref(a)
    print ref
    print a
    print ref() == a
    del a
    gc.collect()
    print ref
    print ref()

func()
</code>
Output:
<code>&lt;weakref at 0x7f4e9a9dbb40; to 'A' at 0x7f4e9a9dbb10&gt;
&lt;__main__.A object at 0x7f4e9a9dbb10&gt;
True
deleted
&lt;weakref at 0x7f4e9a9dbb40; dead&gt;
None
</code>

