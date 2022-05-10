import ctypes
ctypes.windll.user32.GetSystemMetrics()
</code>
This load the dll, but fails on the <code>GetSystemMetrics()</code> call.
The error is : <code>ValueError: Procedure called with not enough arguments (4 bytes missing) or wrong calling convention</code>
I'm pretty sure the function is part of <code>user32.dll</code> and I don't think the arguments are needed according to the documentation, but I can't find a way to tell ctypes all this information.


A:

<code>GetSystemMetrics</code> is a function pointer, which is similar to a callback but passes the context via a different mechanism.  The docs for <code>GetSystemMetrics</code> are pretty transparent about this; it states that it takes an argument <code>nIndex</code> of type <code>int</code> and returns an <code>int</code>.
The problem though is that <code>GetSystemMetrics</code> is the entry point for an exported function.  From the docs:
<blockquote>
<p><code>&lt;code&gt;
