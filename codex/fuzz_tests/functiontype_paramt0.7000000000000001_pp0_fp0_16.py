from types import FunctionType
list(FunctionType(code_obj, globals(), name='test_fn'))
</code>
This is the error I get:
<code>TypeError: 'code' object is not iterable
</code>
I'm pretty sure the function type is iterable, but maybe I'm missing something. What am I doing wrong?


A:

You are trying to instantiate a <code>FunctionType</code> object by passing a code object instead of a function.
The <code>FunctionType</code> class is used for function objects and normally you'd create a function object with the <code>def</code> statement:
<code>def test_fn():
    return 1

test_fn
&lt;function test_fn at 0x7fbbfceb6e60&gt;
</code>
Look at the <code>type</code> of the <code>test_fn</code> object.
<code>type(test_fn)
&lt;class 'function'&gt;
</code>
See, <code>FunctionType</code> is the class of <code>function</code> objects.
