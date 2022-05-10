import ctypes

class S(ctypes.Structure):
    x = 1

print (S().x)
# 1
</code>
When I try to run it on my system I get the following error:
<code>&gt;&gt;&gt; ctypes.Structure
&lt;class 'ctypes.Structure'&gt;
&gt;&gt;&gt; class S(ctypes.Structure):
...     x = 1
&gt;&gt;&gt; print (S().x)
Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'int' object is not callable
</code>
For some reason, my ctypes module is telling me that "int" is not callable. I have no idea why. Can someone please explain why this is happening on my system?


A:

Your example runs just fine on my machine (running Python 3.5.1). The problem is with the variable name <code>x</code>. Try using another name for the variable, for example, <code>foo</code>.
<code>In [
