import types
types.GeneratorType
```

```python
def my_generator():
    yield 2
    yield 2

g = my_generator()
type(g)
```

```python
def my_generator():
    yield 2
    yield 2

g = my_generator()
next(g)
next(g)
next(g)  # raises a StopIteration if there are no more values (because it is an iterator)
```

Python uses generators to handle lazy-evaluated operations, such as in the `itertools` module and in the `range()` function.

Look at `itertools.count()`:

```python
itertools.count()
type(itertools.count())
itertools.count(10)
itertools.count(10, 5)
```

```python
c = itertools.count()
type(c)
next(c)
next(c)
```

```python
c = itertools.count(3)
next(c)
next(
