import ctypes
ctypes.c_int64 = ctypes.c_longlong

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_square = list(map(lambda x:x**2,numbers))
print(list_square)

list_sum = list(map(lambda x,y:x+y, numbers, numbers))
print(list_sum)

list_filter = list(filter(lambda x:x%2==0,numbers))
print(list_filter)

a,b,c = [1,2,3]
print(a,b,c)

d = [1,2,3,4]
d1 = d[1:3] # slice
print(d1)

d2 = list(range(1,10)) 
print(d2)

d3 = d2[::2]
print(d3)

# assignment
num = list(range(1,10))
print(num)

num[2:5] = [10,10,10]
print(num
