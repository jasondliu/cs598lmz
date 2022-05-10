import gc, weakref

class Test(object):
    def __init__(self):
        print 'Test created'
    def __del__(self):
        print 'Test destroyed'

def callback(*args):
    print 'callback:', args

def test():
    t = Test()
    cb = weakref.ref(t, callback)
    print 't:', t
    print 'cb:', cb
    del t
    print 'cb:', cb
    print 'cb():', cb()
    print 'cb():', cb()

if __name__ == '__main__':
    test()
    gc.collect()
    print 'gc.garbage:', gc.garbage
</code>
The output is
<code>Test created
t: &lt;__main__.Test object at 0x7f3e3b8b8c10&gt;
cb: &lt;weakref at 0x7f3e3b8b8e10; to 'Test' at 0x7f3e3b8b8c10&gt;

