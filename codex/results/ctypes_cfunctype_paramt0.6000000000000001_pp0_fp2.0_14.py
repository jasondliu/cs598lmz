import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def callback(x, y):
    return x + y

c_callback = FUNTYPE(callback)

from scipy.optimize import fmin_tnc

fmin_tnc(c_callback, [0, 0], fprime=None, approx_grad=1, bounds=None,
         epsilon=1e-08, scale=None, offset=None, messages=15, maxCGit=-1,
         maxfun=None, eta=-1, stepmx=0, accuracy=0, fmin=0, ftol=-1,
         xtol=-1, pgtol=-1, rescale=-1, disp=None)
</code>
And I got this error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/dist-packages/scipy/optimize/tnc.py", line 573,
