import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        
s = S()

s.x = 1
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    s.x = 1
  File "test.py", line 6, in __setattr__
    super().__setattr__(name, value)
TypeError: __setattr__() missing 1 required positional argument: 'value'
</code>


A:

From the docs:
<blockquote>
<p><code>&lt;code&gt;__setattr__()&lt;/code&gt;</code> is called unconditionally to implement assignment to self.name, even if the class already defines a slot corresponding to name (for example, when self is an instance of a subclass of a built-in type such as <code>&lt;code&gt;int&lt;/code&gt;
