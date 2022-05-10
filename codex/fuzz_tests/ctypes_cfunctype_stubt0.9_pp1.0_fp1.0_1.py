import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2,3)

print fun()
</code>
Throws a <code>TypeError</code> stating <code>exceptions must derive from BaseException</code> (from the ctypes module). I'm assuming this is because <code>(1,2,3)</code> is a tuple and not a subclass of <code>BaseException</code>??
On a Python/Win64/Python27 platform:
<code>&gt;&gt;&gt; ExitProcess = ctypes.windll.kernel32.ExitProcess
&gt;&gt;&gt; ExitProcess(0)
</code>
Throws a <code>SystemExit</code> exception.
What's the meaning behind this behavior? How can I return something else than an exception from a <code>CFUNPYTE</code> callable?


A:

<blockquote>
<p>How can I return something else than an exception from a CFUNPYTE
  callable?</p>
</blockquote>
Any object can be returned because at this point the returned object is just a Python object and is no
