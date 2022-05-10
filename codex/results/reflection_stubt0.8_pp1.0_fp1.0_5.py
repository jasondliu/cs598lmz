fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
```

```python
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
```

```python
fn = lambda: None
fn.__code__ = 1
fn()
```

```python
fn = lambda: None
fn.__code__ = 'a'
fn()
```

```python
fn = lambda: None
fn.__code__ = print
fn()
```

```python
try:
    fn = lambda: None
    fn.__code__ = print
    fn()
except:
    print('code object is コードオブジェクトだけはいじらないでね！')
```
 
## CodeObjects.ipynb

```python
a1 = list(dir(dir))[0]
a2 = list(dir(dir))[4]
a3 = list(dir(dir))[5]
a4 = list(dir(dir))[6
