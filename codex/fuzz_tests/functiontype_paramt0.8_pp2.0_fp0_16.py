from types import FunctionType
list(FunctionType('abc', 'abc', None))
</code>
It errors:
<code>Traceback (most recent call last):
  File "main.py", line 1, in &lt;module&gt;
    list(FunctionType('abc', 'abc', None))
TypeError: 'FunctionType' object is not iterable
</code>
But when I type it to a list, it works:
<code>list([FunctionType('abc', 'abc', None)])
</code>
I want to learn the reason why it doesn't work?


A:

<code>FunctionType</code> is a class, not an object.
Therefore, you can't iterate over it. To create an object from a class, you have to call it.
In your code, you are creating a list from a namedtuple, not a class. A namedtuple is an object.
<code>a = namedtuple('b',['c'])
print(list(a(1)))
</code>
output:
<code>[1]
</code>
If you try to iterate over a class, you will
