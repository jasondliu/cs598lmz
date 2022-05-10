import types
types.MethodType(list.append, 1)

# TypeError: descriptor 'append' of 'list' object needs an argument
</code>
If you want to add methods to your object, you'll have to use the <code>type</code> function.  It should look something like this:
<code>def myfunc():
    print("Hello, world!")

class One:
    def __init__(self):
        pass


One = type('One', (object,), dict(MyOne=One, myfunc=myfunc))
</code>

