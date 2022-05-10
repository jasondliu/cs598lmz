import ctypes
ctypes.CDLL("libc.so.6").srand(rnd.randint(1, 65535))

# Generate a random number of random integers, between 0 and 99, and add them
# to the list 'numbers'.
numbers = []
for i in range(0, rnd.randint(1, 100)):
    numbers.append(rnd.randint(0, 99))

# Print the list.
print(numbers)

# Sort the list.
numbers.sort()

# Print the list again.
print(numbers)
