import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Fizz'[i % 3 * 4::]+'Buzz'[i % 5 * 4::] or str(i) for i in range(1, 101)))).start()

# 5.
# If you have a list of numbers, you can use list comprehension to square all the numbers in the list.
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

# 6.
# You can also use list comprehension to create a list of numbers.
numbers = [x for x in range(1, 11)]
print(numbers)

# 7.
# The following example uses list comprehension to create a list of numbers that are divisible by 3.
numbers = [x for x in range(1, 21) if x % 3 == 0]
print(numbers)

# 8.
# You can use list comprehension with multiple for loops.
numbers = [x + y for x in [10, 30, 50] for y in [20, 40, 60]]

