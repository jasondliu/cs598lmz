import types
types.MethodType(get_grade,student1)

# 给实例绑定的方法，对另一个实例是不起作用的
student2 = Student('Bob','male',16)
student2.get_grade

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score

student1.set_score(100)
student1.score

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动
