import types
types.MethodType(lambda self: 1, None)

# TypeError: unbound method __init__() must be called with A instance as first argument (got nothing instead)
# A.__init__()

# TypeError: unbound method __init__() must be called with A instance as first argument (got int instance instead)
# A.__init__(1)

# TypeError: unbound method __init__() must be called with A instance as first argument (got str instance instead)
# A.__init__('1')

# TypeError: unbound method __init__() must be called with A instance as first argument (got list instance instead)
# A.__init__([])

# TypeError: unbound method __init__() must be called with A instance as first argument (got dict instance instead)
# A.__init__({})

# TypeError: unbound method __init__() must be called with A instance as first argument (got B instance instead)
# A.__init__(B())

# TypeError: unbound method __init__() must be called with A instance as first argument
