fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__code__.__class__(gi)
```

``` python
# generate a list, constant value == [1,1,1,1]
a = [[1] * 4] * 4
```

``` python
# Alternative array declaration as list comprehension
a = [[1 for i in range(4)] for i in range(4)]
```

``` python
# Alternative array declaration as numpy.ndarray
a = numpy.ndarray(shape=(4, 4), dtype=int)
```

``` python
# Add noise to an image using matrix multiplications
im = im * (numpy.random.normal(size=im.shape[:2]) * 0.2 + 1)
```

``` python
# Generate new image using per-pixel arithmetic
im = im * numpy.random.normal(size=im.shape[:2]) + 128
```

``` python
# Data structure comprehension 
a = dict((i,i**2) for i in range(10))
```

``` python
#
