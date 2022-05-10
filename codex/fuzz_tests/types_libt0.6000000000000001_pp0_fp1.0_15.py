import types
types.MethodType(lambda self: None, None, object)

# TypeError: unbound method lambda() must be called with object instance
# as first argument (got nothing instead)
</code>

