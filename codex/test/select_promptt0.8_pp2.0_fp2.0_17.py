import select
# Test select.select function

l1 = [1,2,3]
l2 = ['a','b','c']
l3 = [7,8,9]

read,write,errors = select.select([],[l1,l2,l3])
print('write: ',write)
print('length: ',len(write))
if write:
    print(write[0][0])
else:
    print('empty')
