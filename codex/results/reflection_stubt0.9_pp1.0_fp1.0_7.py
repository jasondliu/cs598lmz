fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code  # segfault
</code>
The new Python interpreter didn't handle this.  The old one did, creating two frames:
<code>Python 3.2a2+ (default:3b87f87ca943, Mar 7 2011, 17:32:18)
[GCC 4.5.1 20100514 (Red Hat 4.5.1-2)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import sys
&gt;&gt;&gt; fn = lambda: None
&gt;&gt;&gt; gi = (i for i in ())
&gt;&gt;&gt; fn.__code__ = gi.gi_code
&gt;&gt;&gt; sys.settrace(lambda *args: None)
&gt;&gt;&gt; fn()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "
