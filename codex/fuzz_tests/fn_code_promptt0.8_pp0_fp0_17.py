fn = lambda: None
# Test fn.__code__.co_varnames == ()
</code>
Python 2.7 or 3.5
<code>&gt;&gt;&gt; fn = lambda: None
&gt;&gt;&gt; fn.__code__.co_varnames
()
</code>
Other Python versions
Try this instead:
<code>&gt;&gt;&gt; from dis import dis
&gt;&gt;&gt; dis(fn.__code__)
</code>
See the Disassembly Objects section of the dis documentation for an example.
FYI:
<code>&gt;&gt;&gt; type(fn)
&lt;type 'function'&gt;
&gt;&gt;&gt; fn.__code__
&lt;code object &lt;lambda&gt; at 0x7fdb3abe3b70, file "&lt;stdin&gt;", line 1&gt;
&gt;&gt;&gt; fn.__code__.co_varnames
()
&gt;&gt;&gt; type(fn.__
