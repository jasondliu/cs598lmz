import gc, weakref

class SomeClass(object):
    def __del__(self):
        print "I'm dead!"

def callback(ref):
    print "I have been deleted!"

x = SomeClass()
x_ref = weakref.ref(x, callback)

del x

print x_ref
# x = None

print len(gc.get_referrers(x))
</code>
output:
<code>I have been deleted!
&lt;weakref at 0x104d28750; dead&gt;
0
I'm dead!
</code>

