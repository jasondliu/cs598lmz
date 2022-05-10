import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(10000000))))).start()

# The above code will print numbers from 1 to 10 million in the background.
# You can do other tasks while this code is running in the background.

# The below code will print numbers from 1 to 10 million in the foreground.
# You cannot do other tasks while this code is running.
for i in range(10000000):
    print(i)

# The below code will print numbers from 1 to 10 million in the foreground.
# You cannot do other tasks while this code is running.
sys.stdout.write('\n'.join(map(str, range(10000000))))
