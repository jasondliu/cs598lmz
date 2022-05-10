import ctypes
ctypes.cast(0, ctypes.py_object)
Segmentation fault
</code>


A:

The reason for the segfault is that the Python <code>py_object</code> struct is not defined. You should define it yourself, by finding out the definition for your Python version and the platform your are on. The <code>ctypes</code> documentation states:
<blockquote>
<p>The py_object and PyObject pointers Python object types are
  platform-specific, they should be instantiated using the <code>&lt;code&gt;Py_FetchPlatformObject()&lt;/code&gt;</code></p>
</blockquote>
Also, you can not cast between pointers that point to different types, the way you did in your example.
Also note that <code>ctypes</code> provides lots of convenience wrappers, you should read the <code>structs</code> section of the documentation.

