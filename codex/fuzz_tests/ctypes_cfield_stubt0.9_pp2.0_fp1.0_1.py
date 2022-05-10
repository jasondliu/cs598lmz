import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print('ctypes.CField: %r' % ctypes.CField)
</code>
And run that against my 3.1 interpreter, it prints:
<code>ctypes.CField: &lt;class '_ctypes._CField'&gt;
</code>
and against Python 3.2 (cmodules):
<code>ctypes.CField: &lt;class 'ctypes._CField'&gt;
</code>
Bingo! The parser is opening <code>_ctypes.py</code> but it's got the wrong kind of <code>CField</code> class, one that is not picklable.
So what can cause this?
<blockquote>
<p>The Python interpreter can be linked to an application written in C or C++</p>
</blockquote>
However, I've never done that—nor has anyone else who's worked on the program.
So what other kinds of "interaction with C" are there?

Compiling with an older version of Python, which then unpickles that pickle on a newer version.
Possibly this; the
