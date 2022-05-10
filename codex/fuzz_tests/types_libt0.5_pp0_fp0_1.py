import types
types.MethodType(method, object)

#把一个类的方法转换成一个静态方法
types.MethodType(method, class)

#把一个类的方法转换成一个类方法
types.MethodType(method, class, class)

#把一个对象的方法转换成一个对象方法
types.MethodType(method, object, class)
```

## 四、类的继承

继承的作用：

- 减少重复代码
- 增强代码的可维护性
- 提高程序的扩展性

### 1、继承的语法

``
