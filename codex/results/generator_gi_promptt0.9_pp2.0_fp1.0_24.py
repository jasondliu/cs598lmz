gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame.
print(gi.gi_code is None)
print(gi.gi_frame is None)
```

#### GeneratorExit

The `GeneratorExit` exception is raised inside a generator to cause it to terminate early.

```python
def gen():
    try:
        yield 1
    except GeneratorExit:
        print('gen.close() called')
    yield 2

for i in gen():
    print(i)

g = gen()
print(next(g))
g.close()  # Causes the generator to throw GeneratorExit inside the generator
try:
    next(g)
except StopIteration:
    print('StopIteration caught')
```

#### Generator not iterable warning

If a generator is called without a value, then it displays a warning.

```python
def gen():
    yield 1

g = gen()
g() # Output: TypeError is not callable

```


### Yield expressions

The `yield` statement is used in generators to create yield expressions.

There are two kinds
