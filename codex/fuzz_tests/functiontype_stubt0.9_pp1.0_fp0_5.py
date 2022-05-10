from types import FunctionType
a = (x for x in [1])
b = FunctionType(a, globals(), 'b')
</code>
The code above produces this error:
<code>NameError: name 'b' is not defined 
</code>
while this code works well:
<code>a = (x for x in [1])
b = StaticMethodType(a, None, object)
</code>
and this
<code>a = (x for x in [1])
b = MethodType(a, None, object)
</code>
According this works for <code>StaticMethodType</code> and <code>MethodType</code> but not for <code>FunctionType</code>, but can I have in a fast way a <code>FunctionType</code> who would do what's done by <code>ClassMethodType</code> for this type of generator?


A:

You are passing in a generator. Try this
<code>from types import FunctionType
a = (x for x in [1])
b = FunctionType(next(a), globals(), 'b')
</code>

