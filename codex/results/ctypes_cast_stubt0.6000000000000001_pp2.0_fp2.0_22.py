import ctypes
ctypes.cast(x, ctypes.py_object).value
#> [1, 2, 3, 4, 5]
```

## Check if a variable is a number

```python
isinstance(x, Number)
```

## Check if a variable is a string

```python
isinstance(x, str)
```

## Check if a variable is a list

```python
isinstance(x, list)
```

## Check if a variable is a tuple

```python
isinstance(x, tuple)
```

## Check if a variable is a set

```python
isinstance(x, set)
```

## Check if a variable is a dictionary

```python
isinstance(x, dict)
```

## Check if a variable is a function

```python
def is_function(x):
    return hasattr(x, '__call__')
```

## Get the type name of a variable

```python
type(x).__name__
```

## Convert a list of
