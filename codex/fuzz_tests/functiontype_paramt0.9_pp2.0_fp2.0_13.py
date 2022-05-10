from types import FunctionType
list(FunctionType(-1) for i in range(5))

# ! [stop1]

# ! [stop2]
from types import FunctionType
list(FunctionType for i in range(5))

# ! [stop2]

########################################
## 4.14 Улучшение функции range() в цикле for

# ! [start]
r = range(0, 100, 4)
print(r)
print(r[10])
print(r[10: 20])
for i in r[::-10]:
    print(i)

# ! [start]

########################################
## 4.15 В отличие от списков, кортежи защищены

# ! [start]
# l = [1, 2, 3, 4]
# l[0] = 10
# t = (1, 2, 3, 4)
# t[0
