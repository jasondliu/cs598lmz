import types
types.MethodType(lambda self: None, None, None)

# -----------------------------------------------------------------------------
# Test code
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod()
