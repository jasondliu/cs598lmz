import ctypes
ctypes.cast(pstr, ctypes.py_object)[0]

# Adding isinstance(pstr, ctypes.py_object) and a unary + to get rid of the error in 2.7
if isinstance(pstr, ctypes.py_object) and not isinstance(pstr, ctypes.c_int):
    if version[0] == 2:
        pstr = +pstr
    else:
        pstr = +pstr[0]

</code>
Here is the code that is giving me an issue as described above in Python 2.7:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; pstr = ctypes.c_char_p("Hello world!")
&gt;&gt;&gt; ctypes.cast(pstr, ctypes.py_object)[0]
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: expected LP_c_long instance instead of c_char_p
</
