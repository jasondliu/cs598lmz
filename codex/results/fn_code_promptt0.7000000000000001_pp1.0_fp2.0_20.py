fn = lambda: None
# Test fn.__code__.co_cellvars etc.
class A:
    def __init__(self, x):
        self.a = x

    def get(self):
        return self.a

a = A(42)
fn = a.get
def fn2(n):
    return a.a * n
print(fn.__code__.co_cellvars)   # ('a',)
print(fn2.__code__.co_freevars)  # ('a',)

"""
14.4.4. __closure__ and __annotations__

The __closure__ attribute of functions holds a tuple of cells that contain the function’s free variables. You can access the current value of the free variables from these cells. For example, the following function returns a closure that returns the average of the values supplied to it:
"""

def make_average():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return average

avg = make_
