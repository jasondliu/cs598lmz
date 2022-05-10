import select
# Test select.select call
print(select.select([], [], [], 0.01))
```

```
['foo', 'bar', 'baz']
```

```
# Python code
a = ['foo', 'bar', 'baz']
print(a[-1])
```

```
baz
```

```
# Python code
a = {'a': 'foo', 'b': 'bar'}
print(a.get('c', 'baz'))
```

```
baz
```

```
# Python code
print('foobar'.replace('foo', 'bar'))
```

```
barbar
```

```
# Python code
a = ('file.ext', 'file2.ext', 'file3.ext')
print(''.join(a).count('.'))
```

```
3
```

```
# Python code
import sys
with open(sys.argv[1]) as f:
    print(f.read())
```
