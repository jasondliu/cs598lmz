fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__module__ = '__main__'

import pdb; pdb.set_trace()
fn()
</code>
This results in the following exception:
<code>$ python3 test.py
&gt; /tmp/test.py(10)&lt;module&gt;()
-&gt; fn()
(Pdb) c
Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    fn()
  File "test.py", line 5, in fn
    fn.__code__ = gi.gi_code
AttributeError: 'generator' object has no attribute 'gi_code'
</code>
However, if I do the same thing using a <code>lambda</code> expression instead of a <code>def</code> statement, it works:
<code>import pdb; pdb.set_trace()
(lambda: None).__code__ = gi.gi_code
(lambda: None)()
</
