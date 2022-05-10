from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])

def test(x):
    return x

d = [a, b, c]

for x in d:
    print(type(x))
    print(type(test))
    print(type(test) == FunctionType)
    if type(x) == FunctionType:
        print('yes')
</code>
The output will be:
<code>&lt;class 'generator'&gt;
&lt;class 'function'&gt;
True
&lt;class 'generator'&gt;
&lt;class 'function'&gt;
True
&lt;class 'generator'&gt;
&lt;class 'function'&gt;
True
</code>
What's the problem?


A:

You are checking the type of the generator, not the function that created it. The generator itself is an object and is a different type.
To check the function that created the generator, look at the <code>gi_code</code> attribute:
<code
