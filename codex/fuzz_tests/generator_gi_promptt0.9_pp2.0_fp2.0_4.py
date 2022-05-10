gi = (i for i in ())
# Test gi.gi_code.__class__.__name__ == 'code'
```

```
>>> get_generator_code(gi.gi_code)
array('b', [124, 0, 0, 0, 1, 0, 0, 0, 10, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 104, 0, 0, 0, 117, 110, 105, 116, 109, 0, 0, 0, 1, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
```

```
>>> from dis import dis
>>> dis(gi.gi_code)
  2           0 LOAD_CONST               1 (0)
              3 YIELD_VALUE
              4 POP_TOP
              5 LOAD_CONST               0 (None)
              8 RETURN_VALUE
```

### Install

### Usage

```python
# sample.
