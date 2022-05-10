from types import FunctionType
a = (x for x in [1])
if type(a) == FunctionType:
    print('a')
else:
    print('b')

for i in a:
    print(i)
print(a.__next__())
print(a.__next__())

a = (x for x in [1,2,3,4,5])

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         print('n=%d' % n)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as
