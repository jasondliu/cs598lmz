fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
print(fn.__closure__[0].cell_contents)
```

```
>>> import dis
>>> dis.dis(fn.__code__)
  1           0 LOAD_GLOBAL              0 (print)
              2 LOAD_DEREF               0 (i)
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
>>> fn()
None
```

#### References:
- https://www.python.org/dev/peps/pep-0477/
- https://stackoverflow.com/a/20368804
- https://stackoverflow.com/a/17133661

### Python Shebang (`#!/usr/bin/env python`)
While it may look like `#!/usr/bin/env python`, the `python` at the end of the shebang is actually optional. This has been confirmed in the Python documentation (which I've confirmed in Ubuntu, MacOS, and Windows by trying it):

> It
