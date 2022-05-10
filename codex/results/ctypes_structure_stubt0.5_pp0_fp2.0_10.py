import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__dict__)
</code>
This prints:
<code>1
2
{}
</code>
So clearly the <code>__dict__</code> attribute is not populated with the fields of the structure.
Is there a way to populate the <code>__dict__</code> attribute with the fields of a <code>ctypes.Structure</code>?


A:

<blockquote>
<p>Is there a way to populate the <code>&lt;code&gt;__dict__&lt;/code&gt;</code> attribute with the fields of a <code>&lt;code&gt;ctypes.Structure&lt;/code&gt;</code>?</p>
</blockquote>
Yes, there is a way:
<code>import ctypes

class S(ctypes.Structure):
    x
