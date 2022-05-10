import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# Question 7:
# What is the output of this code?
class Test:
    def __init__(self):
        self.x = 0

    def increment(self):
        self.x += 1

t1 = Test()
t2 = Test()
t1.increment()
print(t1.x, t2.x)

# Output: 1 0

# Question 8:
# What is the output of this code?
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

# Output: 3 3 3

# Question 9:
# What is the output of this code?
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(x):
           
