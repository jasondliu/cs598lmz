fn = lambda: None
gi = (i for i in ())
fn.__code__ = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(gi.__length_hint__(fn))

# 1
fn.__code__ = (1, 2, 3, 4, 5, 6, 7, 8)
print(gi.__length_hint__(fn))

# 2
fn.__code__ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(gi.__length_hint__(fn))

# 1
fn.__code__ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print(gi.__length_hint__(fn))
```

```
# The maximum number of items of sequence is 2 ** 9 * 2 ** 9 * 2 ** 9
#  1. 2 ** 9 * 2 ** 9 * 2 ** 9 = 2 ** 27
#  2. 2 ** 27 = 2 ** 9 * 2 ** 9 * 2 ** 9
#  3. 2 ** 9 * 2 ** 9 * 2 ** 9 = 2
