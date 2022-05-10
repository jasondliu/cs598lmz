from types import FunctionType
list(FunctionType(list(FunctionType.__dict__.values()).pop().__code__.co_consts[2]))

#3.85. Дан список a. Вернуть список, состоящий из тех же элементов, для которых a[i] + a[i + 1] = 0
a = [1, -1, 2, -2, 3, -3, 4]
[(a[i],a[i+1]) for i in range(len(a)-1) if a[i] + a[i + 1] == 0]

#3.86. Дан кортеж a. Вернуть элементы, которые встречаются в a бол
