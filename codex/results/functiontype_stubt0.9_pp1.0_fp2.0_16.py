from types import FunctionType
a = (x for x in [1])
print(type(a) is GeneratorType)

a1 = __import__('__main__')
b = a1.x
print(type(b) is int)

a = [1, 2, 3]
for i, v in enumerate(a):
    print(i, v)

def a(x):
    return x

for i in dir(a):
    if '__' not in i:
        print(i)

import numpy as np
a = np.matrix(np.zeros(10))
print(a.shape)

import pandas as pd
data = pd.read_excel('C:\\Users\\user\\Desktop\\test.xlsx')
