import types
types.MethodType(m, obj)
# <bound method obj.m of <__main__.obj object at 0x10b2c6fd0>>

obj.m()
# 'm of obj'
```

```python
# 方法绑定到另一个对象上（创建新的对象）
obj2 = types.MethodType(m, obj)
obj2()
# 'm of obj'
```

```python
# 函数绑定到另一个对象上（创建新的对象）
obj3 = types.MethodType(m, 'obj3')
obj3()
# 'm of obj3'
```

### 3.2 构造对象的时候绑定

```python
# 在实例化的时候
