import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 42
print fun()
</code>

<blockquote>
<p><em>Does this hold true for other languages as well?</em></p>
</blockquote>
It's not universal, but it's very common.
In C++ (at least up to C++11) and Haskell, closures are by default not allowed to reference variables in the environment where they are created, unless those variables are explicitly marked as being <code>mutable</code>, or unless a special syntax is used to make them accessible (the <code>-&gt;</code> syntax in C++ for lambdas, and the <code>where</code> keyword in Haskell).
In Python, the default is the opposite: all variables in the environment where a function is created are accessible by default. In order to prevent this, you have to explicitly use the <code>nonlocal</code> keyword.

