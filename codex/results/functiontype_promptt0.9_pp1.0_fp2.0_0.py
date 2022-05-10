import types
# Test types.FunctionType
def test_types_functiontype():
    if (True):
        # the simplest function
        def func():
            # try to access attribute that does not exist
            #var_2 = 3 + func.var_3
            var_2 = 3 + funcAttributes[0]
            # multiply 2 by itself
            var_2 = var_2 * var_2
            # returnt the value
            return var_2
        # add an attribute to the function
        funcAttributes = []
        # execute the function
        var_1 = func()
        # now test the types
        # exercise typeof operator
        assert type(var_1) is types.IntType
        assert type(func) is types.FunctionType
        assert type(var_1) is int
        assert type(func) is function
        # exercise isinstance operator
        assert isinstance(var_1, types.IntType)
        assert isinstance(fun
