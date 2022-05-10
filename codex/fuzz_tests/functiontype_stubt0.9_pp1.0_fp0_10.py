from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a,FunctionType))

b = [1]
print(b)
print(isinstance(b,FunctionType))
'''
'''
#把a变成生成器对象
a = (x for x in range(10))
print(a.__next__()) #指导取出下一个元素
print(a.__next__()) 
print(a.__next__()) 

for i in a :
    print(i)'''

#斐波那契数列的生成器
# def fn(n):
#     a,b= 0,1
#     for i in range(n):
#         a,b = b,a+b
#         yield a

# for i in fn(15):
#     print(i)


#简单的封装
# def inifo(name,age):
#     print("my
