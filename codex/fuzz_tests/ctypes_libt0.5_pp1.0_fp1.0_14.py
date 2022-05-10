import ctypes
ctypes.windll.kernel32.SetConsoleTitleW('FizzBuzz')

#FizzBuzz
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

#FizzBuzz - using a list
for i in range(1, 101):
    print(['', 'Fizz'][i % 3 == 0] + ['', 'Buzz'][i % 5 == 0] or i)

#FizzBuzz - using a list and a dictionary
for i in range(1, 101):
    print({True: 'FizzBuzz', i % 3 == 0: 'Fizz', i % 5 == 0: 'Buzz'}.get(True, i))

#FizzBuzz - using a list and a dictionary and a ternary operator
for i in range(1, 101):
    print({True: 'FizzBuzz', i % 3 == 0: 'Fizz', i
