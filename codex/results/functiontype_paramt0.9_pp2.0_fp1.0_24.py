from types import FunctionType
list(FunctionType(
    FunctionType.__code__, globals(), FunctionType.__name__,
    FunctionType.__defaults__, FunctionType.__closure__),)
</code>
python version: 3.6.5
result:
SyntaxError: can't write function outside function (cell)
current solution:
<code>def list_(*args, **kwargs):
    return list(*args, **kwargs)
</code>
expected result:
<code>[&lt;class 'types.FunctionType'&gt;]
</code>
why in function list or tuple passed a function is not callable?


A:

actually, Python3 syntax error.
If the interpretor is outputting the error
<code>SyntaxError: can't use function (type code) as parameter
</code>
this is a compatability issue because this specific syntax is not supported for Python3.
In Python2, I can get the desired output as follows:
<code>&gt;&gt;&gt; list(FunctionType)
[&lt;class 'types.FunctionType'&gt;]
&gt
