import sys, threading
threading.Thread(target=lambda: sys.stdout.write(raw_input()+'\n')).start()

# a = raw_input()
# b = raw_input()
# print int(a)+int(b)

# def fib(n):
#     if n < 3:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# n = int(raw_input())
# print fib(n)

# n = int(raw_input())
# for i in range(n):
#     print i**2

# a, b = [int(x) for x in raw_input().split()]
# print a+b if a < b else a-b

# a = int(raw_input())
# b = int(raw_input())
# print a if a > b else b

# a = int(raw_input())
# b = int(raw_input())
# print a if a < b else b

# a = int(raw_input())
# b = int(raw_input())

