fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
```

```
TypeError: 'generator' object is not callable
```

###### 古怪的赋值

```python
a = b = c = 1
```

```python
def f():
    print(a)
    a = 2
    print(a)

f()
```

```
UnboundLocalError: local variable 'a' referenced before assignment
```

```python
def f():
    a = 2
    print(a)
    a = 2
    print(a)

f()
```

```
2
2
```

###### 变量名

```python
x = "ab"
y = "cd"
print(x + y)
```

```
abcd
```

```python
x = "ab"
y = "cd"
print(x + y)
```

```
abcd
```

###### 列
