import types
types.ClassType

# but this does not
if isinstance(MyClass, ClassType):
    print('class def style')
else:
    print('class literal style')
# class literal style

# yet this does
if type(MyClass) == ClassType:
    print('class def style')
else:
    print('class literal style')
# class def style
</code>
Boolean truth of an instance by identity
When an instance is checked in a boolean context, it is considered <code>False</code> only if it is an instance of <code>bool</code> with value <code>False</code>, or a zero-length string, or a zero length tuple, or <code>None</code>. 
So, there is no way to find out if an instance is a <code>True</code> boolean or a non-empty string or tuple or something else by truthiness.
However, an instance can be checked for a distinct identity by the <code>is</code> operator.
<code>a = True
b = 'some_string'
c = ()
a is True
# True
b is '
