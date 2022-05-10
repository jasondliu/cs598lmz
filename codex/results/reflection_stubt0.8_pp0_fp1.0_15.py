fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
fn.__name__ = "test"
print(w_e(fn, True))
</code>
... and it's a <code>TypeError</code>!
<code>&gt;&gt;&gt; fn = lambda: None
&gt;&gt;&gt; gi = (i for i in ())
&gt;&gt;&gt; fn.__code__ = gi.gi_frame.f_code
&gt;&gt;&gt; fn.__name__ = "test"
&gt;&gt;&gt; print(w_e(fn, True))
Traceback (most recent call last):
  File "&lt;pyshell#10&gt;", line 1, in &lt;module&gt;
    print(w_e(fn, True))
  File "&lt;pyshell#7&gt;", line 9, in w_e
    traceback.print_stack(f)
  File "C:\Python35\lib\traceback.py", line 385, in
