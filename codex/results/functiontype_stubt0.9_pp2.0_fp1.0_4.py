from types import FunctionType
a = (x for x in [1])
print type(a)

#b = (FunctionType(x) for x in[])
#for i in b:
#    print i

#c = (FunctionType() for x in [1,2,3])


for i in [1,2,3]:
    for j in [4,5,6]:
        print i*j
        
for i in [1,2,3]:
    for j in 'abcd':
        print i,j

for i in 'abcd':
    for j in [1,2,3]:
        print i,j
        
        
L = [1,2,3]
for L in []:
    pass
print L
