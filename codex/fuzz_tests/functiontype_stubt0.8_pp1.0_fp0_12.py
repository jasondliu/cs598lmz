from types import FunctionType
a = (x for x in [1])
type(a)

a = list(range(3))
b = [i**2 for i in range(3)]

print(list(map(lambda x: x**2, a)))

def is_odd(x):
    return x % 2 == 1

print(list(filter(is_odd, a)))
print(list(map(is_odd, a)))

print(list(filter(lambda x: x % 2 == 1, range(10))))

# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     days[1] = 29
#
# print(sum(days[:month - 1]) + day)



#  参数检查器


