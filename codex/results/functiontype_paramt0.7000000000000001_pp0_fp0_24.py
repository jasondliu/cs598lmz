from types import FunctionType
list(FunctionType("x", "y") for x in range(3))

#Output:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 1, in &lt;genexpr&gt;
NameError: name 'y' is not defined
</code>
The code above is equivalent to <code>[FunctionType("x", "y") for x in range(3)]</code>. In the middle of the <code>genexpr</code>, the compiler encounters <code>FunctionType("x", "y")</code> and tries to evaluate it. However, <code>y</code> is not defined, so an error is thrown.
Note that the <code>return</code> statements in a <code>genexpr</code> are implemented as <code>yield</code>s, so your list comprehension is the same as:
<code>def f():
    for x in range(3):
        yield FunctionType("x", "y")
</code>
and <code>
