from types import FunctionType
list(FunctionType(FunctionType, object).__code__.co_names)
>>>['lambda1', 'lambda2']

f_co_names(0)
f_co_names(1000)
```

К ограниченному алфавиту относится также имя `class` — вспомните, что это такое:

```python
>>> type(object)
<type 'type'>
>>> set([type(object), TypeError])
NameError: name 'TypeError' is not defined

f_co_names("class")
f_co_names(1000)
```
Переменные — окошки - возможности компилятора для применения м
