import types
types.MethodType(method, obj)

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图
