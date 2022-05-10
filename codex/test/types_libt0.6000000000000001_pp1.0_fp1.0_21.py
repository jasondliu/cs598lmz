import types
types.FunctionType

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

bart.get_grade()
lisa.get_grade()

bart.age = 8
bart.age

type(bart)
type(lisa)

def print_score(std):
    print('%s: %s' % (std.name, std.score))

print_score(bart)
print_score(lisa)

