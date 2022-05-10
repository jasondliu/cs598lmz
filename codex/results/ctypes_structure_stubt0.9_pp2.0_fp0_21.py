import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(1)


print(S(1))
</code>
The above code prints <code>&lt;__main__.S object at 0x0000026AE8A2C9F0&gt;</code>
I want to change this to return something like:
<code>&lt;__main__.S object at 0x000002D1A51AC750&gt; (1,1)
</code>


A:

I think you want <code>__str__</code>:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(1)
    def __str__(self):
        return "S({}, {})".format(self.x.value, self.y.value)

print(S(1))
</code>
This gives:
<code>S(1, 1)
</code>

