from types import FunctionType
list(FunctionType(1,2,3))
```

При создании функции существует еще одна возможность контроля: `global` и `nonlocal`.

```python
def out():
    global _x
    _x = 1
    print('1:',_x)
    def inn():
        nonlocal _x
        _x = 2
        print('2:',_x)
    inn()
    print('3:',_x)
out()
print('4:',_x)
```

`global` позволяет брать значения переменных с уровня, указанного заранее в настр
