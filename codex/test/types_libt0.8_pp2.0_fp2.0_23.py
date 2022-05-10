import types
types.ClassType

# but this does not
if isinstance(MyClass, ClassType):
    print('class def style')
else:
    print('class literal style')
# class literal style

# yet this does
