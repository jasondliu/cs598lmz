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


"""
String manipulation

https://practice.geeksforgeeks.org/explore.php?page=practice&practice=String

1. Reverse a String

https://www.hackerrank.com/challenges/reverse-a-string/problem

2. Capitalize!

https://www.hackerrank.com/challenges/capitalize/problem

3. Capitalize! 2

https://www.hackerrank.com/challenges/capitalize-2/problem


