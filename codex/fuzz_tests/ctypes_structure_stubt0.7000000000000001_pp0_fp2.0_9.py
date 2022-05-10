import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class D(S):
    pass

print D.x
print D.y
</code>
This returns:
<code>1
&lt;Field type=c_long, ofs=0, size=4&gt;
</code>
However, the ctypes documentation says the following:
<blockquote>
<p>The <code>&lt;code&gt;_fields_&lt;/code&gt;</code> attribute of a Structure class defines the fields of that
  structure. It is a sequence of 2-tuples, one tuple for each field,
  containing the name of the field and the ctypes type. The attribute is
  optional, but without it the Structure is useless.</p>
</blockquote>
And in the reference manual:
<blockquote>
<p>If the _fields_ attribute is defined, it must be a sequence of name,
  type pairs, where the type is a ctypes data type describing the field
  type.</p>
</blockquote>
Is there a way
