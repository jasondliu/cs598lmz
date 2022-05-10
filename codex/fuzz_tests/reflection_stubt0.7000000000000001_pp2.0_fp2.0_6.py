fn = lambda: None
gi = (i for i in ())
fn.__code__ = (
            None, # argcount
            0, # nlocals
            0, # stacksize
            0, # flags
            b'', # codestring
            (), # constants
            (), # names
            (), # varnames
            '', # filename
            '', # name
            1, # firstlineno
            b'' # lnotab
            )
fn.__code__.co_freevars = (gi,)
del gi

print(fn.__code__.co_freevars)
</code>

Python 3.4.1
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: readonly attribute
</code>

Python 3.4.4
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: readonly attribute
</code>

Python 3.7.0
<code>(&lt;cell at 0
