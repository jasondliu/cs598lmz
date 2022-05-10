import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input().swapcase()+'\n')).start()


# 3.
# f = open('text.txt', 'w')
# f.write(str(input()))
# f.close()


# 4.
# n = int(input())
# summ = 0
# for i in range(2, n+1):
#     summ += int(input())
# print(summ)


# 5.
# n = int(input())
# a = [0]
# for i in range(n):
#     a.append(int(input()))
#
# summ = 0
# for i in range(1, len(a)):
#     summ += a[i] * a[i-1]
# print(summ)


# 6.
# a = input().split()
# print(*a[::-1])


# 7.
# n = int(input())
# if n % 2 == 0:
#     print(int(n / 2))
# else:
#     print(int(
