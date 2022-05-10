import io
class File(io.RawIOBase):
  ...
</code>
but it doesn't work.
<code>&gt;&gt;&gt; f = File()
&gt;&gt;&gt; f
&lt;__main__.File object at 0x7f1a3a3d3e48&gt;
&gt;&gt;&gt; print(f)
&lt;__main__.File object at 0x7f1a3a3d3e48&gt;
</code>
This is not a problem for <code>open()</code>, it just returns the value from <code>io.open</code>
<code>&gt;&gt;&gt; open('/dev/null')
&lt;_io.BufferedReader name='/dev/null'&gt;
&gt;&gt;&gt; io.open('/dev/null')
&lt;_io.BufferedReader name='/dev/null'&gt;
</code>
Strangely enough, <code>io.StringIO</code> works as expected.
<code>&gt;&gt;
