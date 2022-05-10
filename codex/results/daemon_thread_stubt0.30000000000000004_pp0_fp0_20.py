import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

print('Hello')
thread.join()
print('World')

# Output:
# Hello
# ....World

# Example 2
import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

print('Hello')
time.sleep(3)
print('World')

# Output:
# Hello
# ...World

# Example 3
import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start
