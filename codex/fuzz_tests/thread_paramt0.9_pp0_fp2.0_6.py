import sys, threading
threading.Thread(target=lambda: (sys.stdout.write('thread\n'), sys.exit())).start()
main()
</code>
<blockquote>
<p>Output (Windows 7): (note <code>&lt;code&gt;main&lt;/code&gt;</code> starts running only after the <code>&lt;code&gt;i = 0&lt;/code&gt;</code> line is done)</p>
</blockquote>
<code>thread
main
main
</code>


A:

Because you're exiting after writing to <code>stdout</code>. This is effectively an arbitrary <code>stdout</code> buffer flush.
From the Python docs:
<blockquote>
<h2>exit functions</h2>
<p>A trivial example of an exit function can be coded as follows:</p>
<pre><code>&lt;code&gt;import sys

def exitfunc():
     print "exit callback!"

sys.exitfunc = exitfunc
&lt;/code&gt;</code></pre>
<p>The exit function is
