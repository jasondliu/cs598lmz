import types
types.MethodType(lambda self: self.x, None, A)

# This should fail
types.MethodType(lambda self: self.x, None, B)

# This should fail
types.MethodType(lambda self: self.x, None, C)

# This should fail
types.MethodType(lambda self: self.x, None, D)

# This should fail
types.MethodType(lambda self: self.x, None, E)

# This should fail
types.MethodType(lambda self: self.x, None, F)

# This should fail
types.MethodType(lambda self: self.x, None, G)

# This should fail
types.MethodType(lambda self: self.x, None, H)

# This should fail
types.MethodType(lambda self: self.x, None, I)

# This should fail
types.MethodType(lambda self: self.x, None, J)

# This should fail
types.MethodType(lambda self: self.x, None, K)

# This should fail
types.MethodType
