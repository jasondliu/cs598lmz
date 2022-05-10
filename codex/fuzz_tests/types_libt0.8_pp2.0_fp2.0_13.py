import types
types.FunctionType

# another example
def func1(name, age, *args, gender=None, **kwargs):
    print(name, age, args, gender, kwargs)
# positional arguments
# func1(1,2,3,4,5,6)
func1('Alex', 16, 'Python', 'Java', 'Ruby', gender='Male', c=1, d=2, e=3)

# keyword arguments
func1(name='Alex', age=16, gender='Male', c=1, d=2, e=3)

# mixed arguments
func1('Alex', 16, gender='Male', c=1, d=2, e=3)

# give values to all keyword arguments
def func2(name, age, gender=None, city=None, job=None):
    print(name, age, gender, city, job)
# func2('Alex', 16, gender='Male', city='Beijing', job='Engineer')

# give value to only some of keyword arguments
func2('Alex', 16, gender='Male', job='Engineer')

