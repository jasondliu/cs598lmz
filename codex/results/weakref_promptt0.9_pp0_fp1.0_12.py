import weakref
# Test weakref.ref()
class Cow:
    def Moo(self):
        print ("Moo")

c = Cow()
r = weakref.ref(c)
# r().Moo() #'function' object has no attribute 'Moo'
c.Moo()

c = None #deleted
r().Moo() 

# should return None
# print (r())
print (r)

# string addition test
s = "Hello"
s = s + " world"
print (s)
print('A\nB\nC')

# ---------------------------------------------------
# Function test
def Sum(x,y):
    return x + y

print (Sum(5,5))

# Recursion test
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

print (Fibonacci(10))


# ---------------------------
# Module test
import time
print (time.clock())

import random
print (random.randint(
