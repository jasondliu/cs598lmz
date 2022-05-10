import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
In this case, the <code>ctypes</code> module does not import the <code>type</code> function, but uses a type provided by the Python runtime.  So, in the main program, the <code>type</code> function is a <code>builtin</code>, whereas in the <code>ctypes</code> module it is a <code>type</code> object.
Since <code>type</code> is a builtin, its <code>__name__</code> attribute is <code>"type"</code>, and its <code>__module__</code> attribute is the empty string.  The <code>__module__</code> attribute of <code>ctypes.CField</code> is <code>"ctypes"</code>, and its <code>__name__</code> attribute is <code>"CField"</code>.  So, the <code>typing</code> module needs to know how to deal with the case that either <code>__module__</code> is the empty string or <code>__name__</code> is <code>"CField"</
