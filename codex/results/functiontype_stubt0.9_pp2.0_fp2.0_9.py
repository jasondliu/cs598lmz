from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a==b)
print(type(a)==type(b))
print(FunctionType==type((lambda x:x)))

import operator
from functools import partial
from itertools import *
import math
print(partial(math.pow, 2))

print(operator.isMappingType({}))

from collections import *

#maybe a bad idea, but works

def add_inverse(x = 0, op = operator.add, discriminator = set):
    inv = discriminator((y,-y) for y in x)
    return x.union(inv)

def query_answers(user_input, validator, asked = 0):
    answer = user_input()
    if answer in validator(answer):
        return answer
    else:
        print("incorrect input")
        return query_answers(user_input, validator, asked + 1)

def choose_from(answers):
    print(*(map(str,answers)))
    @fun
