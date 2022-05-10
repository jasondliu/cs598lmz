import types
types.MethodType(lambda self: self.x + self.y, None, A)
</code>
<code>MethodType</code> takes the function, the instance and the class as arguments. The instance is used to resolve the <code>self</code> argument, the class is used to resolve the <code>cls</code> argument.
<code>lambda</code> expressions are not methods. They are functions, and as such, they don't have a <code>self</code> argument.

