import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()

# 2.6
# The following code is supposed to print out the square root of all the numbers from 0-99, but it throws an exception instead. Fix the code so that it works properly:

# for i in range(100):
#   print(i, end='')
#   print(math.sqrt(i))

import math
for i in range(100):
    print(i, end='')
    print(math.sqrt(i))

# 2.7
# The following code is supposed to print out the square root of all the numbers from 0-99, but it throws an exception instead. Fix the code so that it works properly:

# for i in range(100):
#   print(math.sqrt(i))

import math
for i in range(100):
    print(math.sqrt(i))

# 2.8
# The following code is supposed to print out the square root of all the numbers from 0-99, but it throws an exception instead. Fix the code so that it works
