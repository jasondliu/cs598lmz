import sys, threading
threading.Thread(target=lambda: sys.stdout.flush(), args=()).start()
############################################################
def add(a,b):
    print(a+b)
    return a+b

def sub(a,b):
    print(a-b)
    return a-b

def mul(a,b):
    print(a*b)
    return a*b

def div(a,b):
    print(a/b)
    return a/b

def val(a):
    return a

def sqrt(a):
    print(a**(1/2))
    return a**(1/2)

def po(a,b):
    print(a**b)
    return a**b

def sin(a):
    print(math.sin(a))
    return math.sin(a)

def cos(a):
    print(math.cos(a))
    return math.cos(a)

def logm(a,b):
    print(math.log(a,b))
    return math.log(a,
