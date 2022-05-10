import types
types.MethodType(a, None, Foo()) # "a" is an unbound method
```

```python
>>> types.MethodType(a, Foo(), None) # "a" is a bound method
```

```python
>>> types.MethodType(a, Foo(), Foo()) # "a" is a bound method
```

```python
>>> types.MethodType(1, Foo(), Foo())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

---

## 정리
`types` 모듈에는 실수로 잘못 사용하는 것들을 방지할 수 있는 함수들이 존재한다.

`type()`, `isinstance()`, `issubclass()`,
