import gc, weakref

class SimpleObject:
    def __init__(self, name):
        self.name = name
    def __repr__ (self):
        return 'SimpleObject({0})'.format(self.name)


def on_finalize(arg):
    print('on_finalize({0})'.format(arg))

obj = SimpleObject('obj')
f = weakref.finalize(obj, on_finalize, 'obj goes away')
del obj
f
</code>
Since the object is now gone, I'd expect the code to print out <code>'obj goes away'</code>, but it doesn't.
<code>gc.collect()
weakref.finalize(obj, on_finalize, 'obj goes away')  # Here is called with 'obj'
</code>
I don't understand why the finalizer is called when the object is still around?


A:

<blockquote>
<p>I don't understand why the finalizer is called when the object is still around?</p>
</blockquote>
Because you explicitly told it to:
<code
