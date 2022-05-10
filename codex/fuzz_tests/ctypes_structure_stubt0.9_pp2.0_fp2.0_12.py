import ctypes

class S(ctypes.Structure):
    x = {"x": 5}

assert type(S.x) is ctypes.Structure
</code>
By contrast, if I try to make the same thing in Python 3, the assertion fails:
<code>import ctypes

class S(ctypes.Structure):
    x = {"x": 5}

print(S.x)
</code>
Is it it a bug (and so I should report it somewhere), or is it a "feature"? On which grounds?


A:

It seems that when trying to access an attribute as <code>S.x</code> in Python 3, you get a <code>property</code> that's created from a <code>dict</code> through the <code>dict.__getattribute__</code> method -- the doc for which is copied below.
<code>TypeError: x is not a valid attribute of c_double
</code>
<code>def __getattribute__(self, key):
  try:
    return object.__getattribute__(self, key)
  except AttributeError:
    try:
      return self[key]
