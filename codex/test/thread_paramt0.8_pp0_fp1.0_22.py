import sys, threading
threading.Thread(target=lambda: sys.stdout.write("foo")).start()
print("bar")

# Just an empty file
with open("file.txt", "w") as empty:
    pass

# Equivalent to `echo Hello World`.
print("Hello World")

# Terminal input (e.g. `read foo`).
foo = input("Please type something: ")
print("You said", foo)

# Random number with `shuf -i 0-100 -n 1`
import random
print('Your lucky number is {}'.format(random.randint(0, 100)))

# Random number between 1 and 6 with `shuf -i 1-6 -n 1`.
print(random.randint(1, 6))

# System uptime with `uptime`.
from datetime import datetime
import os
uptime = os.popen("uptime").read()
print('System uptime is {}.'.format(uptime))

