import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello my dear student", "This is a message", 1)

print("Hello my dear student")

def fahrenheit(T):
    return (9.0/5)*T + 32

print(fahrenheit(0))

def fahrenheit2(T):
    return (9.0/5)*T + 32

def celsius(T):
    return (5.0/9)*(T-32)

temp = [0,22.5,40,100]

F_temp = map(fahrenheit2,temp)

print(list(F_temp))

C_temp = map(celsius,temp)

print(list(C_temp))

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

abc = map(lambda x,y,z:x+y+z, a,b,c)

print(list(abc))

#reduce(function, list)
from funct
