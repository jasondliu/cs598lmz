from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])
def f(a,b,c):
    return a,b,c

print(type(f))
print(type(f(a,b,c)))
print(tuple(f(a,b,c)))
print(type(tuple(f(a,b,c))))

# N = int(input())
# for i in range(N):
#     for j in range(N):
#         pass


# def f(a,b,c):
#     print(a,b,c)
#
# f(1,2,3)
# f(a=1,b=2,c=3)
# f(1,c=3,b=2)
# f(1,2,c=3)

# def f(a,b,c):
#     print(a,b,c)
#
# f(1,2,3)
# f(a=1,b=2,c=3)
# f(
