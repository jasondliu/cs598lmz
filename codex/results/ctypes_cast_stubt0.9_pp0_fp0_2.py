import ctypes
ctypes.cast(0, ctypes.py_object)
#this looks like its the same as the cast we are doing to the py_type ptr, but it works differently. this local variable will point to 0, so the dereference will dereference it to get 0 - which is an invalid pointer.
</code>
This is the relevant section of the ctypes documentation:
<blockquote>
<p>Since the address of the object is actually known, calling f is faster.
  a[0] calls the overload that returns a PyObject*, which then has to be dereferenced twice (once for a, and once for a[0]).</p>
</blockquote>
The key difference between the two variables is that the second one is dereferenced before the <code>(+)</code> or <code>[]</code> operators are applied. The first variable has the address stored in the object itself, so it can be accessed quickly. The second variable is storing the address of the address, so <code>a[0]</code> will evaluate to <code>a.value[0]</code> which is <code>address[0]</code> which is
