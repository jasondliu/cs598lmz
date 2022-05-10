import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input().strip()[::-1])).start()

import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input()[::-1])).start()

import sys
threading.Thread(target=lambda: sys.stdout.write(input()[::-1] + '\n')).start()

# input()[::-1]

# Write your code here
lines = sys.stdin.readlines()
for line in lines[::-1]:
    sys.stdout.write(line)


