import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
print S.x.__class__, type(S.x)
</code>
This is the result:
<code>&lt;type 'instancemethod'&gt; &lt;type 'member_descriptor'&gt;
</code>
As you can see, although both methods retrieve the same value when called, they have different types.  <code>member_descriptor</code> is a base type for many things, including both <code>method_descriptor</code> and <code>wrapper_descriptor</code>.  So, really, you're asking what the difference is between an instance method, and a descriptor of type <code>member_descriptor</code>.
This is covered in the Descriptor HowTo Guide, and I'll try to sum it up:

Descriptors are Python classes that overload the attribute access operators; in the case of <code>member_descriptor</code> you're interested in, the <code>__get__</code> and <code>__set__</code> methods.  These allow you to intercept attribute accesses, and perform
