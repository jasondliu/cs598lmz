from types import FunctionType
list(FunctionType('f'))

def _sum(a, b):
    return a + b

_sum(1, 2)

_sum(2, 2)

_obj = list()

_obj.append(1)

_obj.append(2)

_obj.append(3)

_obj.append(4)


_obj

_obj2 = [x for x in _obj if x > 2]

generator_adder = lambda x, y: x + y

generator_adder(1, 2)

def quick_adder(a, b):
    return a + b

quick_adder(1, 2)

quick_adder(2, 2)

a = 10
a

a

l = [1, 'a', a]

for x in l:
    print(x)


print('hello world')


get_dictionary = dict()

get_dictionary


get_dictionary = {}

get_dictionary

_list = list()

_list

_str = str()

