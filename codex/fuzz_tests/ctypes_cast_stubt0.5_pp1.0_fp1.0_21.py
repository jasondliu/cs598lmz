import ctypes
ctypes.cast(0, ctypes.py_object).value

# This should print "Hello World", but it doesn't
&gt;&gt;&gt; ctypes.cast(0, ctypes.py_object).value
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: NULL pointer access
</code>
So, I'm stumped. Is there any way around this?


A:

You can't cast a <code>NULL</code> pointer to a <code>py_object</code> because the <code>py_object</code> structure contains a field <code>ob_refcnt</code> which is a reference count. If you could cast a <code>NULL</code> pointer to a <code>py_object</code>, you could have a reference count of <code>0</code> which would be wrong.
You can cast a <code>NULL</code> pointer to a <code>py_object *</code> and dereference it, but you can't cast it to a <code>
