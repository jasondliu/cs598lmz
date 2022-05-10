fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(b'', (object,), {})()
fn ()
```

```
Traceback (most recent call last):
  File "code5.py", line 6, in <module>
    fn ()
TypeError: 'code' object is not callable

```
