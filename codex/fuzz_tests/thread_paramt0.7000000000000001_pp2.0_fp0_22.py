import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 1 ')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2 ')).start()
print('Main ')

print()

# Output:
# Main Thread 2 Thread 1
#
# Main Thread 1 Thread 2
#
# Main Thread 1 Thread 2
#
# Main Thread 1 Thread 2
#
# Main Thread 1 Thread 2
#
# Main Thread 1 Thread 2
#
# Main Thread 1 Thread 2
#
# Main Thread 1 Thread 2
#
# Main Thread 1 Thread 2
#
# Main Thread 1 Thread 2

# 3.2
# Run the following code many times. What do you notice about the output?

import threading
x = 0
def increment():
    global x
    x += 1

def thread_task():
    for _ in range(100):
        increment()

def main_task():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t
