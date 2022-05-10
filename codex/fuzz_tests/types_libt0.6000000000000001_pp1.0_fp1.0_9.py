import types
types.MethodType(foo, U)
</code>
is not allowed, but
<code>class U: pass
def foo(self): print(self)
types.MethodType(foo, U)
</code>
is allowed.
The above are instances of the following:
<code>class U: pass
class V:
    def foo(self): print(self)

types.MethodType(V.foo, U)
</code>
So, in the first case, the <code>foo</code> function is bound to <code>V</code> and then, in the second case, <code>V</code> is bound to <code>U</code>.
So, the first case is not allowed.

