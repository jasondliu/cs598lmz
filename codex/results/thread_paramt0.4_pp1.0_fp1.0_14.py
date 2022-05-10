import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,101)))).start()

# FizzBuzz in a single line of Python (using list comprehension)
print '\n'.join(['Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,101)])

# FizzBuzz in a single line of Python (using list comprehension)
# with a function
def fizzbuzz(n):
    return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,n+1)]

# FizzBuzz in a single line of Python (using list comprehension)
# with a function and map
def fizzbuzz(n):
    return map(lambda x: 'Fizz'*(not x%3) + 'Buzz'*(not x%5) or str(x), range(1
