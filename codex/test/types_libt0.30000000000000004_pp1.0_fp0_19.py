import types
types.MethodType(lambda self, x: self.x + x, None, A)

# TypeError: unbound method &lt;lambda&gt;() must be called with A instance as first argument (got nothing instead)
