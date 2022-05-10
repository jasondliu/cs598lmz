from types import FunctionType
list(FunctionType('none'.lower, globals()))
</code>
However, I need a way to make this loop over all instances of a specific type of class in the global namespace. I tried doing:
<code>my_class = type('my_class', (object,), {})
a = my_class()
b = my_class()

my_class_instances = []
for name in globals():
    if isinstance(globals()[name], my_class):
        my_class_instances.append(globals()[name]
</code>
This works except it adds the class definition itself as an instance (since it is an instance of my_class). How do I make this loop over only instances and not the class itself?


A:

You could use the <code>inspect.isclass</code> function.
<code>import inspect

my_class_instances = []
for name, val in globals().items():
    if inspect.isclass(val) and issubclass(val, my_class):
        my_class_instances.append(val)

