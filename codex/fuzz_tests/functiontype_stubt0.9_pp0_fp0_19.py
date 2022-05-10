from types import FunctionType
a = (x for x in [1])
b = {1:1}
c = [1,2,3]
d = 'hello'
e = 1
f = True
g = {():1}
h = FunctionType

print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h),sep=',')
'''

'''
# Sort
a = [1, 2, 5, 7, 8]
b = [4, 6, 2, 5, 7]
c = a+b
print(sorted(c))
'''

'''
# List Comprehension
x = [1, 2, 3, 4, 4, 5, 1]

# Loop with if clause
y = [foo for foo in x if foo >= 4]
print(y)

# Loop with if/else
z = [bar if bar >= 4 else 'l' for bar in x]
print(z)
'''

'''
# Read lines from  file
r = open('hosts.txt', 'r')


