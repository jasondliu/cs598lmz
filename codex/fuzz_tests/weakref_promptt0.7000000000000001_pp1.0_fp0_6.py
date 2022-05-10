import weakref
# Test weakref.ref()

class foo(object):    
    pass

x = foo()
y = foo()

# Create a weakref to y
a = weakref.ref(y)

# Create a weakref to x, but with a callback
def callback(object):
    print(object)
w = weakref.ref(x, callback)

del y
del x

print(a())
print(w())

print('end')
</code>
Output:
<code>None
None
None
end
</code>
In the example above, the callback function is called when x is deleted, but not when y is deleted. Why is that?


A:

According to the PEP, the <code>__del__()</code> method is not guaranteed to get called.
<blockquote>
<p>The del statement is never guaranteed to work in Python, and in
  particular, it will not work in the presence of reference cycles. For
  example:</p>
<pre><code>&lt;code&gt;class Node:
    def __init__(self, value
