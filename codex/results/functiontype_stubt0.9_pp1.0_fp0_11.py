from types import FunctionType
a = (x for x in [1])
#print(type(a))
gen = (x for x in range(10))
for i in gen:
    print(i)
print('gen done')

gen2 = (x for x in range(10))
print(type(gen2))

#r = map(lambda x: x * 2, gen2)
#print(list(r))
print(type(map))

a = (1,2,3)
print(type(a))

#print(FunctionType(a))


def ddd(a, b):
    return (b, a)

ll = ddd(1,2)

print(ll)
