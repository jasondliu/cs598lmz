import ctypes
ctypes.cdll.LoadLibrary("/home/pi/Desktop/numpy-1.9.2/numpy/core/_multiarray_umath.so")
ctypes.cdll.LoadLibrary("/home/pi/Desktop/numpy-1.9.2/numpy/core/umath.cpython-34m.so")
</code>
However, I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/pi/Desktop/numpy-1.9.2/numpy/core/_multiarray_umath.so", line 4, in &lt;module&gt;
  File "/usr/local/lib/python3.4/dist-packages/numpy/core/_multiarray_umath.cpython-34m-arm-linux-gnueabihf.so", line 2, in &lt;module&gt;
ImportError: No module named 'numpy.core._multiarray_umath'
</code
