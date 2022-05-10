import types
types.MethodType
class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count = Student.count + 1

    def how_many(self):
        print("total %s students" % Student.count)

# 如果要给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score = score
Student.set_score = types.MethodType(set_score,Student)

bart = Student("Bart")
bart.set_score(100)
print(bart.score)


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添
