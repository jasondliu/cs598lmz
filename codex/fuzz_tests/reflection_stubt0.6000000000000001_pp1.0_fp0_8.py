fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.send.__code__
fn()
```

```
$ python3.7 -m timeit 'fn()'
100000 loops, best of 5: 4.97 usec per loop
```

```
$ python3.7 -m timeit 'fn()'
100000 loops, best of 5: 3.82 usec per loop
```

```
$ python3.7 -m timeit 'fn()'
100000 loops, best of 5: 5.15 usec per loop
```

```
$ python3.7 -m timeit 'fn()'
100000 loops, best of 5: 3.83 usec per loop
```


```
$ python3.7 -m timeit 'fn()'
100000 loops, best of 5: 3.91 usec per loop
```


```
$ python3.7 -m timeit 'fn()'
100000 loops, best of 5: 3.9 usec per loop
```

```
$ python3.7 -m timeit 'fn()'

