import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __init__(self, *args):
        super().__init__(*args)
        self.x = 42

c = S()
print(c.x)
</code>
The output is <code>0</code> instead of <code>42</code>.
What am I doing wrong?


A:

You will get the same behavior if you define <code>x</code> as:
<code>self.x = ctypes.c_int(42)
</code>
This is because <code>c_int</code> is a class and <code>x</code> is an instance of that class. Therefore, you don't initialize it with an <code>int</code> but with another instance of the same class. As the <code>__init__</code> method of <code>c_int</code> doesn't have a default value for <code>value</code> you are effectively instantiating it as <code>c_int()</code>. This is equivalent to <code>c_int(0)</code> as <code>0</
