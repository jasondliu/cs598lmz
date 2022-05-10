import types
types.ModuleType.__getattr__ = lambda self, name: types.ModuleType(self.__name__ + '.' + name)
</code>
This will make <code>import module.submodule</code> the same as <code>import module</code>. You will have to use <code>import module.submodule as module</code> if you want to use the new <code>module</code>.

