import ctypes
ctypes.cast(ctypes.c_int, 1)
# ctypes.cast(1, ctypes.c_int) # error

# ######################################################################################################################

# string formatting
print('My name is {0} and I\'m {1} years old!'.format('John', 25))

m = 'My name is {name} and I\'m {age} years old!'.format(name='John', age=25)
print(m)

m = 'My name is {0} and I\'m {1} years old!'.format(*['John', 25])
print(m)

m = 'My name is %s and I\'m %d years old!' % ('John', 25)
print(m)

m = 'My name is {0} and I\'m {age} years old!'.format('John', age=25)
print(m)

# ######################################################################################################################

# integer division
print(5 // 2)
print(-5 // 2)
print(5 / 2)
print(-5 / 2)
print(5 % 2)

