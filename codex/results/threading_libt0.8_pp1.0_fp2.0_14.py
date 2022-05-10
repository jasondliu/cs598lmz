import threading
threading.enumerate()
</code>
<blockquote>
<blockquote>
<blockquote>
<p>[&lt;_MainThread(MainThread, stopped 4887)&gt;]</p>
</blockquote>
</blockquote>
</blockquote>
<code>p.wait()</code> blocks the thread it was called from until the process has completed.
<blockquote>
<blockquote>
<blockquote>
<p>p.wait()
      &gt;&gt;&gt; threading.enumerate()
      [&lt;_MainThread(MainThread, stopped 4887)&gt;]</p>
</blockquote>
</blockquote>
</blockquote>
<code>p.communicate([input])</code> blocks the thread it was called from until the process has completed.
<blockquote>
<blockquote>
<blockquote>
<p>p.communicate([input])
      (&lt;stdout&gt;, &lt;stderr&gt;)
      &gt;&gt;&gt; threading.
