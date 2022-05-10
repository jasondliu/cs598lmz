import types
types.MethodType(f, None, Student)
# 允许给一个实例绑定的方法，把它调用时的第一个参数自动绑定到实例本身
# 通过这种方法，我们在编写类的时候，就可以随时根据需要添加功能了

#
# 还可以用属性来定义
# 下面的s.name = 'Michael' 实际上是调用了s.set_name('Michael') 方法
class Student(object):
    @property
    def score(self):
        return self._score
    @score.set
