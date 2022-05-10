import types
types.__dict__

types.__dict__['__builtins__']['open'] = open
</code>
It works, but I would like to know if there is a better solution.


A:

I assume that you are trying to call <code>open</code> from a module that has been compiled with <code>Py_OptimizeFlag</code> and that you have access to the source code of this module.
If so, then you can add the following line to the top of the module:
<code>__builtins__ = __import__('__builtin__')
</code>
This will force the module to import the builtins from <code>__builtin__</code> instead of <code>__builtins__</code> and therefore your replacement will take effect.

