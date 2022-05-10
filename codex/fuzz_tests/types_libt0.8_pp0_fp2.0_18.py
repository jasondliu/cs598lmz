import types
types.NoneType
```
### callable
* 判断一个对象是否是可以被调用（函数，方法，类，类实例）
```
callable(max)
callable([])
```
### isinstance
* 判断一个对象是否是类的实例
```
isinstance([], list)
```
### issubclass
* 判断一个类是否是另一个类的子类，或者判断一个对象的类型是否是另一个类的子类
```
issubclass(User, UserBase)
issubclass(User, object)
issubclass(User, (UserBase, object))
```
### hasattr

