import types
types.SimpleNamespace(foo=1)

from types import SimpleNamespace
SimpleNamespace(foo=1)
</code>
I can import the first one, but not the second.
<code>In [7]: %paste
&gt;&gt;&gt; from types import SimpleNamespace
&gt;&gt;&gt; SimpleNamespace(foo=1)

In [8]: %paste
&gt;&gt;&gt; from types import SimpleNamespace
&gt;&gt;&gt; SimpleNamespace(foo=1)
Traceback (most recent call last):

  File "&lt;ipython-input-8-f0c8a8e4f7a4&gt;", line 1, in &lt;module&gt;
    SimpleNamespace(foo=1)

NameError: name 'SimpleNamespace' is not defined
</code>
Why is this?


A:

This is a known issue in IPython.
https://github.com/ipython/ipython/issues/5229

