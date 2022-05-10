import select
# Test select.select
import select
import time

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()

end = time.time()
print('Took %.3f seconds' % (end - start))

from select import select
def slow_systemcall():
    select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()

end = time.time()
print('Took %.3f seconds' % (end - start))
 
# Lesson 3: Executing Modules as Scripts
# Python programs can be run as scripts in the shell or executed in the interpreter.
# The script is run in a namespace called __main__.
# The __name__ variable is set to __main__ when the module is run as a script.
# In Python 3, __main__ can be used to set the __name__ variable to __main__.
# The if __name__ == '__main
