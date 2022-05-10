import ctypes
ctypes.cast(my_user_lib.test, ctypes.c_int)
test_3 = my_user_lib.test
test_3()
</code>
I receive the error:
<code>Traceback (most recent call last):
  File "/home/bob/Desktop/test.py", line 8, in &lt;module&gt;
    my_user_lib.test
ValueError: function test not found
</code>
I suspect that this is because my <code>lib.so</code> is not compiled correctly. I checked that I was including the right gcc version by typing <code>echo $CXX</code> which gives me <code>/usr/bin/g++</code> which is the same as my <code>/usr/bin/gcc</code> version. I checked this by typing <code>gcc --version</code> which gives me <code>gcc (GCC) 7.3.0</code>. So it seems to be the case that I am using gcc version 7.3.0.
I am not really sure what I need to do so that I could call my library
