from types import FunctionType
a = (x for x in [1])
type(a)
FunctionType

s = 'he' 'll' 'o'
print(s)

_name = 'Hong'
__name = 'Fred'
print(_name, __name)

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print(list1[0:1:1])
print(list2[2:])

tup = ('physics', 'chemistry', 1997, 2000)
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2;
print(tup3)
print('test' in tup)
print(tup + tup1 + tup2)  # ('physics', 'chemistry', 1997, 2000, 12, 34.56, 'abc', 'xyz')
print(tup.index(1997))
print(tup[1])
del tup

dict1 = {'Name': 'Zara', 'Age
