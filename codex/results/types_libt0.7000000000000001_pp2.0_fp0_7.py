import types
types.CodeType(len(code.co_code), code.co_nlocals, code.co_stacksize, code.co_flags, code.co_code, code.co_consts, code.co_names, code.co_varnames, code.co_filename, code.co_name, code.co_firstlineno, code.co_lnotab)
```

Since we already have the code object, we can simply use the `types` module to construct a new code object that is equivalent to our original one.

Why would we want to do this?

Sometimes, in order to protect against a potential vulnerability, we will want to prevent the execution of any code object or module. This can be accomplished using the `imp.acquire_lock()` and `imp.release_lock()` functions. However, if we decide to do this, we will need to also provide an alternative means of executing our code. In this case, it's useful to be able to re-construct code objects from their bytecode.

## Further Reading

* [types -- names for built-in types](https://docs.python.
