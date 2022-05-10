import types
types.SimpleNamespace(**dict(a=1, b="b"))
```

```python
import types
o = types.SimpleNamespace(a=1)
o
```

```python
o.a
```

```python
o.b = "b"
o.b
```

```python
o
```

```python
{'a': 1, 'b': 'b'}
```

```python
o.__dict__
```

```python
{'a': 1, 'b': 'b'}
```

```python
o.__dict__['a'] = 2
o
```

```python
o.__dict__
```

```python
{'a': 2, 'b': 'b'}
```

```python
# 実は、dictで辞書式（文字列をキーとして、値をメンバー変数として使
