import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

class A(object):
    f = fun

a = A()
a.f()
</code>
<blockquote>
<p>Traceback (most recent call last):   File "", line 1, in
     File "/Users/kimdonghee/anaconda2/lib/python2.7/site-packages/IPython/core/interactiveshell.py", line 2885,
  in run_code
      exec(code_obj, self.user_global_ns, self.user_ns)   File "", line 11, in 
  TypeError: 'CFUNCTYPE' object is not callable</p>
</blockquote>
<code>a.f()</code> gives <code>TypeError: 'CFUNCTYPE' object is not callable</code> but <code>fun()</code> doesn't give that error.


A:

When you use <code>@FUNTYPE</code> to decorate a function, the function is not compiled. Instead, the function object is replaced by a <code>CFUNCT
