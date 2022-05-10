import gc, weakref

class A(object):
    def __init__(self, data):
        self.data = data
    def __del__(self):
        print 'A.__del__'

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print d['primary'].data
del a
gc.collect()
print d['primary'].data
</code>
I get the output:
<code>10
A.__del__
10
</code>
So, I am confused.  I thought that the weakref.WeakValueDictionary() would not hold a reference to the object, but it seems to be doing just that.  Can someone explain what is happening here?


A:

<code>weakref.WeakValueDictionary()</code> does not hold a reference to the object.
The object is still referenced by the variable <code>a</code>.
You can see that if you change the code to:
<code>del a
gc.collect()
print d['primary'].data
</code>
Then you will get:

