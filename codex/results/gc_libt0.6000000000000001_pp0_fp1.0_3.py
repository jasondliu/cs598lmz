import gc, weakref

def my_dest(obj):
    print('my_dest', obj)

wr = weakref.ref(gc.collect, my_dest)

print(gc.collect())
print(wr)
print(gc.collect())
print(wr)

</code>
And the output is:
<code>0
&lt;weakref at 0x7fcfa8c2f2d0; dead&gt;
0
&lt;weakref at 0x7fcfa8c2f2d0; dead&gt;
</code>
I don't understand why the callback isn't called.


A:

The <code>gc.collect</code> function is a built-in, which means that it is not a Python object and cannot be weak-referenced.  The documentation for <code>weakref.ref</code> says:
<blockquote>
<p>If the referent is an object (not a class or a function), it should be
  weakly referenceable; that is, it should have a <code>&lt;code&gt;__weak
