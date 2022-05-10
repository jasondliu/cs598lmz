from types import FunctionType
a = (x for x in [1])
b = (x for x in [1,2])
c = False
Foo = type('Foo', (), {'a':a, 'b':b, 'c':c})
f = Foo()

print(isinstance(f.a, FunctionType), type(f.a))
print(isinstance(f.b, FunctionType), type(f.b))
print(isinstance(f.c, FunctionType))

print(list(f.a()))
print(list(f.b()))
</code>
This is the output I get:
<code>False &lt;class 'generator'&gt;
False &lt;class 'generator'&gt;
False
[1]
[1, 2]
</code>
What exactly is 'generator' here? A generator is a function it seems, how can it be a class?


A:

<code>class</code> is a special keyword in Python that creates a <code>class</code> object.
<code>generator</code> is an object, inheriting from the <code>object
