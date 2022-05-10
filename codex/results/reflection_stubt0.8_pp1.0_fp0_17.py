fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
for _ in range(100):
    fn()
```

## Reference
* [CVE-2017-1000158](https://bugs.python.org/issue30385)
