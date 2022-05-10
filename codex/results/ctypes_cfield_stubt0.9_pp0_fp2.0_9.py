import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def f(*args):
    print(args)

print(f.__code__.co_argcount)
for i in f.__code__.co_varnames:
    print(i)
</code>
This just give me :
<code>1
args
</code>


A:

You can't get names of variables passed in the <code>*args</code> tuple in Python. You can only get their values. Even if you named the tuple by typing <code>def f(*x):</code>, the code would still show up in <code>co_varnames</code> as <code>x</code>, not as <code>f</code>.
Just an anecdote: TypeScript (a typed superset of JavaScript) does feature function definitions of the form <code>function (...args: string[]) { ... }</code>, which gives you the type of each element of the <code>args</code> array, but not its name.

