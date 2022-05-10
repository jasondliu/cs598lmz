import types
# Test types.FunctionType on Test.function1 and Test.function2.
print(isinstance(Test.function1, types.FunctionType))
print(isinstance(Test.function2, types.FunctionType))

# Test isfunction on Test.function1 and Test.function2.
print(inspect.isfunction(Test.function1))
print(inspect.isfunction(Test.function2))

# Test types.MethodType on Test.function1 and Test.function2.
print(isinstance(Test.function1, types.MethodType))
print(isinstance(Test.function2, types.MethodType))

# Test ismethod on Test.function1 and Test.function2.
print(inspect.ismethod(Test.function1))
print(inspect.ismethod(Test.function2))
</code>
When I run it, the output is
<code>False
True
False
True
False
True
False
True
</code>
Any idea why <code>inspect.isfunction</code> and <code>inspect.ismethod</code> return <code>True
