import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# https://www.hackerrank.com/challenges/py-hello-world/problem
print("Hello, World!")

# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# https://www.hackerrank.com/challenges/python-division/problem
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

