import _struct
# Test _struct.Struct is not C compatible.
print(_struct.Struct("i").unpack(bytes(4)))  # [0]
print(_struct.Struct("i").unpack(bytes(5)))  # ValueError: unpack requires a bytes object of length 4

# Now test _struct.Struct is C compatible.
print(_struct.Struct("i").unpack(bytes(4), use_c=True))  # [0]
print(_struct.Struct("i").unpack(bytes(5), use_c=True))  # [0]
```

# Benchmark

`./bench.py`

```text
python3.7:

Struct.unpack:
Ran 50000 tests in 0.129 s
Accuracy is {'correct': 50000, 'wrong': 0}

Struct.unpack C:
Ran 50000 tests in 0.099 s
Accuracy is {'correct': 50000, 'wrong': 0}

unpack:
Ran 50000 tests in 0.079 s
Accuracy is {'correct': 50000, 'wrong': 0}

p
