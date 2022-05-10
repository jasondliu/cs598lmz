fn = lambda: None
gi = (i for i in ())
fn.__code__ = []
gi.__code__ = None
fn()
```

```bash
$ python3 ./test_function.py 
Traceback (most recent call last):
  File "./test_function.py", line 15, in <module>
    fn()
  File "/home/bopjesvla/venvs/tester/lib/python3.6/inspect.py", line 830, in getfullargspec
    raise TypeError('{!r} is not a Python code object'.format(func))
TypeError: <lambda> is not a Python code object

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./test_function.py", line 15, in <module>
    fn()
  File "/home/bopjesvla/venvs/tester/lib/python3.6/inspect.py", line 833, in getfullargspec
    raise ValueError('unsupported callable') from ex
ValueError: unsupported callable

During handling of the above exception, another exception occurred
