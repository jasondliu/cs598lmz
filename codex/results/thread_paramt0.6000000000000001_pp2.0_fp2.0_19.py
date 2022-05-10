import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
'''

# 一行Python编写计算器
# eval('4 + 5')

# 一行Python编写死循环
# while True: pass

# 一行Python编写马格努斯三项式
# [((-1) ** (n - k)) * (n - k + 1) / k for n in range(1, int(input()) + 1) for k in range(1, n + 1)]

# 一行Python编写返回两个数的最大公约数
# lambda a, b: b if a % b == 0 else lambda a, b: a if b % a == 0 else lambda a, b: a * b / (lambda a, b: a if a > b else b)(*map(lambda a, b: a if b == 0 else b, (a, b), (b
