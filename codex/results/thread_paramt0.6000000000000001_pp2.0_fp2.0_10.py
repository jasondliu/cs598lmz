import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Threading\n')).start()

# String concatenation
print('String' + ' concatenation')

# List indexing
print([0, 1, 2][1])

# List slicing
print([0, 1, 2][1:])

# Function definition
def f(x): return x + 1
print(f(3))

# Function application
print(map(lambda x: x + 1, [0, 1, 2]))

# if-else
print('If-else' if True else 'else')

# For loop
print('For')
for i in [0, 1, 2]: print(i)

# While loop
print('While')
i = 0
while i < 3:
    print(i)
    i += 1

# Classes
class C:
    def m(self):
        print('method')

print('Class')
C().m()

# Exceptions
try:
    raise Exception('Exception')
except:
    print('Exception')

# With statement
with open('/
