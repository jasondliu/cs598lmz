import types
types.FunctionType.__call__ = new.instancemethod(__call__, None, types.FunctionType)

def __call__(self, *args, **kwargs):
    print("calling function", self)
    return self.__old_call__(*args, **kwargs)

types.MethodType.__call__ = new.instancemethod(__call__, None, types.MethodType)
</code>

