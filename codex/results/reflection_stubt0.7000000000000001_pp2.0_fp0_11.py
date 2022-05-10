fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__

# 将 fn 转换为可调用对象
fn()
```

### 使用 `marshal` 序列化二进制代码

``` python
import marshal

code = compile('print(42)', 'foo.py', 'exec')
data = marshal.dumps(code)

code = marshal.loads(data)
exec(code)
```

### 使用 `pickle` 序列化二进制代码

``` python
import pickle

code = compile('print(42)', 'foo.py', 'exec')
data = pickle.dumps(code)

code = pickle.loads(data)
exec(code)
```

## 通过 `eval()` 函数执行可执行代码

`eval()` 函数的
