import types
types.MethodType(lambda self, value: self.__setattr__('_x', value), None, object)

ImportError: No module named types
</code>
But, I can still run the module. Any idea?
Thanks!


A:

To import a module you need to add it to the <code>sys.path</code> list. You can do that explicitly or by using <code>PYTHONPATH</code> as @jfs said.
You can use <code>os.path.join</code> to combine elements of the path.

