import types
types.FunctionType = types.LambdaType

def unapply(argv):
    """The type of an unapply method."""
    assert isinstance(argv, types.TupleType), (
        "Unapply's argv argument must be a tuple: %s." % argv
    )

    assert len(argv) == 1, (
        "Unapply's argv argument must be a 1-tuple: %s." % argv
    )

    arg0, = argv

    assert issubclass(
        arg0, types.TupleType
    ), "Unapply's argv argument must have a tuple as its first element: %s." % argv
    
    return types.FunctionType

def implementation(argv):
    """The type of an implementation."""
    assert isinstance(
        argv, (types.TupleType, types.ListType)
    ), "Implementations' argv argument must be a tuple or list: %s." % argv

