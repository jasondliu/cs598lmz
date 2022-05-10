import types
# Test types.FunctionType

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def pow(a, b):
    return a ** b

def fsum(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

def fsorted(lst):
    new_list = sorted(lst)
    return new_list

def ffilter(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i] > 0:
            new_list.append(lst[i])
    return new_list

def fapply(a):
    return a * a

def freduce(a, b):
    return a + b

def fmax(lst):
