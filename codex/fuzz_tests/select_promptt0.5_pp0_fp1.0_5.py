import select
# Test select.select()

import time

start = time.time()
print(select.select([sys.stdin], [], [], 5))
# If input is entered before the timer runs out, select.select() will return
# ([sys.stdin], [], []), otherwise it will return ([], [], [])
print(time.time() - start)

# select.select() can also be used to monitor multiple file descriptors:
start = time.time()
print(select.select([sys.stdin, open('poem.txt')], [], [], 5))
print(time.time() - start)
