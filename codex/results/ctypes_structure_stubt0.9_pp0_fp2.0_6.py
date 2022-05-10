import ctypes

class S(ctypes.Structure):
    x = 4

print S.x                  # 4
S.y = 5
print S.y                  # 5
</code>
Since I'm fine with the <code>class</code>es not inheriting anything in the first place, is there an easy way to do this using decorators or metaclasses?
Bricolage:
<code>In [1]: class S(ctypes.Structure):
   ...:     x = 4
   ...:

In [2]: print S.x
4

In [4]: S.y = 5

In [5]: S.y
Out[5]: 5
</code>
The way I do it now:
<code>def dynamically_add_fields_to_class(class_):
    class_.x = 4
    class_.y = 5

class S(ctypes.Structure):
    pass

dynamically_add_fields_to_class(S)
</code>


A:

<blockquote>
<p>I'm fine with the classes not inheriting anything in the first place</p>
</blockquote>
