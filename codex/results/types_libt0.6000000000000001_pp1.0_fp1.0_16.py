import types
types.MethodType(__modify_method__, None, types.ModuleType('test'))
</code>
So you can use it to modify the method of any module you want:
<code>types.MethodType(__modify_method__, None, my_module)
</code>

