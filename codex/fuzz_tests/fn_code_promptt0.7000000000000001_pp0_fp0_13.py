fn = lambda: None
# Test fn.__code__
fn.__code__

# Expected:
# <code object <module> at 0x10c2b3c40, file "", line 1>
```

```python
fn.__code__.co_argcount
# Expected:
# 0
```

```python
fn.__code__.co_varnames
# Expected:
# ()
```

```python
fn.__code__.co_freevars
# Expected:
# ()
```

```python
fn.__code__.co_cellvars
# Expected:
# ()
```

```python
fn.__code__.co_filename
# Expected:
# ''
```

```python
fn.__code__.co_name
# Expected:
# '<module>'
```

```python
fn.__code__.co_lnotab
# Expected:
# ''
```

```python
fn.__code__.co_stacksize
# Ex
