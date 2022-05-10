import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def dump(obj):
    for key, value in obj.__dict__.items():
        print('  {} --&gt; {}'.format(key, value))

print('S:')
dump(S)
print()

print('S.x:')
dump(S.x)
print()

print('type(S):')
dump(type(S))
print()

print('type(S.x):')
dump(type(S.x))
print()

print('type(type(S.x)):')
dump(type(type(S.x)))

</code>
Output:
<code>S:
  _fields_ --&gt; [('x', &lt;class 'CField'&gt;)]
  __dict__ --&gt; &lt;attribute '__dict__' of 'Structure' objects&gt;
  __doc__ --&gt; Base class for all Structure classes
  __module__ --&gt; ctypes
  _abstract_ --&gt; False
  _anonymous_ --&gt; False
