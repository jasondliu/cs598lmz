import gc, weakref

class C(object):
    pass

c = C()

def f():
    print(c)

w = weakref.ref(c, f)

c = None

gc.collect()

print(w)
</code>
I get the output:
<code>&lt;__main__.C object at 0x7f8b7c0f6d68&gt;
None
</code>
How can I get the output <code>&lt;__main__.C object at 0x7f8b7c0f6d68&gt;</code> without the <code>None</code>?


A:

The <code>None</code> is printed by <code>print(w)</code>.
You could change the callback function to not print anything:
<code>def f():
    pass
</code>

