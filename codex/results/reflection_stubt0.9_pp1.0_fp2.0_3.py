fn = lambda: None
gi = (i for i in ())
fn.__code__ = lambda: gi
fn.__globals__ =  {}
fn.co_stacksize = 65535
execute_code(fn.__code__().next)
print(subprocess.run("./vuln", shell=True, input=b"A\x7d\x08\x40", stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode("utf8"))
```

This is the end

```
Das Ende der Welt
```
