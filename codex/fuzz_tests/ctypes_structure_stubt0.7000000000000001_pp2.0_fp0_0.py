import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16()
    y = ctypes.c_int32()

print S()

print S().x.value is None
print S().y.value is None

S().x.value = 5
S().y.value = 6

print S().x.value
print S().y.value
</code>
Here, I create a <code>ctypes.Structure</code> with two members, a short and a long. When I print out the structure, I get a string representation of the structure, which, in this case, is <code>&lt;class '__main__.S'&gt;</code>. When I print out the values of the members, I get <code>None</code>, because they are not yet assigned. When I assign the members, to 5 and 6 respectively, I can print out the values, and they are 5 and 6.
The problem is, when I print out the structure again, instead of getting:
<code>&lt;class '__main__.S'&gt;
</code>
I get:
<code>&lt;__main__
