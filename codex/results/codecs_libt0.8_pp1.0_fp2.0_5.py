import codecs
codecs.open
print(((1+(5**0.5))/2)**10)

def compute(string, value = 0):
    for i in list(string):
        if i.isupper():
            value += 1
        else:
            value -= 1
    return value

def compute2(string, value = 0):
    for i in list(string):
        value += ord(i) - 64
    return value



def is_triangle(num):
    if (((1+(5**0.5))/2)**num).is_integer():
        return True
    else:
        return False



def is_triangle2(num):
    x = (-1 + ((1+8*num)**0.5))/2
    if x.is_integer():
        return True
    else:
        return False

words = []

with open("C:/Users/jkearns/Desktop/Euler Project/Project Euler 42.txt","r") as f:
    for line in f:
        for i in line.replace('"'
