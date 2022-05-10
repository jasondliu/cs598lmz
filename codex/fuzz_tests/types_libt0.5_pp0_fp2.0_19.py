import types
types.MethodType(process, self)
</code>
I would like to add a new method to an object, but I don't know how to do it.
I have tried this:
<code>def process(self, data):
    print("Processing...")
    return data

import types
types.MethodType(process, self)
</code>
But I get this error:
<code>NameError: name 'self' is not defined
</code>
I have also tried this:
<code>import types
types.MethodType(process, self)
</code>
But I get this error:
<code>TypeError: descriptor '__get__' requires a 'method' object but received a 'function'
</code>
How can I add a new method to an object?


A:

You can create a class and then add the method to it.
<code>class foo:
    def __init__(self):
        self.x = 1

def process(self, data):
    print("Processing...")
    return data

foo.process = process
</code>
