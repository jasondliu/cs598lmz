from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
testcaseval = testcase()
print(type(testcaseval))
assert type(testcaseval) == FunctionType
c = testcaseval(a)
assert c == 1

a = (x for x in [1,2,3])
b = (x for x in [1,2,3])
c = testcaseval(a)
assert c == 3


a = (x for x in [1])
b = (x for x in [2,2])
c = testcaseval(a)
assert c == 2

a = (x for x in [1,2])
b = (x for x in [2,2])
c = testcaseval(a)
assert c == 2
child1 = ChildClass()
child2 = ChildClass()
child1.n = 10
child2.n = 20
print(child1.n)

assert child1.n == 10
assert child2.n == 20
