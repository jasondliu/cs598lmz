import types
types.ModuleType.__getattribute__ = new_getattr
</code>

This is a bit of a hack, and I'm not sure if it will work with all modules.

