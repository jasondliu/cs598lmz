fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__module__ = '__main__'

# Create a new function that can be called.
fn = types.FunctionType(gi.gi_code, globals(), '<lambda>', (), 0, None)

# Call the function.
fn()
```

```
Traceback (most recent call last):
  File "./test.py", line 11, in <module>
    fn()
TypeError: <lambda>() takes no arguments (1 given)
```

What!?

But it does take an argument! It's just that the argument is the `gi` object.

```
def fn():
    return gi

fn()
```

```
<generator object <genexpr> at 0x10d6a0f68>
```

## What's going on here?

Let's look at the stack trace, but this time, let's use the `inspect` module to get the source code of the function.

```
import inspect
