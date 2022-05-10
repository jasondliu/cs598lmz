import sys, threading
threading.Thread(target=lambda: sys.stdout.write('A\n')).start()
threading.Thread(target=lambda: sys.stdout.write('B\n')).start()
threading.Thread(target=lambda: sys.stdout.write('C\n')).start()
print('D') # Use print() from Python 3.X, not Python 2.X's sys.stdout.write().

# print("hello", end='')
# print("world")
#
#  print("cat", "dog", "mouse", sep=', ')

# import sys
# def myprint(s): # Print with comma separator to stdout
#     sys.stdout.write(s + ',')
# myprint('spam')
# myprint('ham')
# myprint('eggs')

# import sys
# def myprint(s): # Print with comma separator to stdout
#     sys.stdout.write(s + ' ')
# myprint('spam')
# myprint('ham')
# myprint('eggs')


# def f(x):
