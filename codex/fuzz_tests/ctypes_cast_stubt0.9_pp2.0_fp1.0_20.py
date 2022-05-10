import ctypes
ctypes.cast(arg, ctypes.py_object).value = a # is a
</code>
the last line works because <code>PyObject*</code> do not need to be dereferenced it is a pointer to object and not just object. 
Is there any reason to prefer one notation over other?


A:

I would say the first version was a mistake and the second is better, since it means exactly what it says. The CFFI documentation even (as of August 2015) says:
<blockquote>
<p>The preferred way to get a pointer to a Python object is to cast the argument given in <code>&lt;code&gt;int&lt;/code&gt;</code> or <code>&lt;code&gt;long&lt;/code&gt;</code> form to <code>&lt;code&gt;void*&lt;/code&gt;</code>, rather than use the <code>&lt;code&gt;void(py_object)&lt;/code&gt;</code> type:</p>
<pre><code>&lt;code&gt
