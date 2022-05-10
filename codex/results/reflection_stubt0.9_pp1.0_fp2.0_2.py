fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
```

* `gi` **must** be **empty**;
* https://github.com/python/core-workflow/pull/60#discussion_r402596551
* https://bugs.python.org/issue40207 (Python 3.10+)
* https://bugs.python.org/issue38301

## How it works?

* `load_global` operation (& *global* bytecode) is used to lookup the global `f` and push it onto the top of the stack;
* `call_function` operation (& *call* bytecode) is used to invoke `f`;
* `f` returns an **empty** generator;
* `gi` generator is then **assigned** to the `fn.__code__` to modify the code object;
* `fn()` call invokes `gi.__next__()` which then throws the `StopIteration` exception rebounded from `f`.

## Related
