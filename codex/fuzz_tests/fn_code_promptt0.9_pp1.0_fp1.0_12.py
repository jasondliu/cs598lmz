fn = lambda: None
# Test fn.__code__ exist in Python 3 (but not in Python 2)
_has_py3_code_type = getattr(fn.__code__, 'co_lnotab', False)
if _has_py3_code_type:
    def __code_type_function():
        return type(lambda: None).__code__

    def __code_type_method():
        return type([].__contains__).__code__

    def __code_type_generator():
        return type((lambda: (yield))().send).__code__

    def __code_type_descriptor():
        return type(int.__add__).__code__

    def __code_type_builtin():
        return type(object.__repr__).__code__

    for cls in object, type, object, object, object, object, object, object, object, object, object, type, int, type,  object.__repr__, object.__init__, object.__new__:
        assert __code_type_function()[:2] == __code_type_method()[
