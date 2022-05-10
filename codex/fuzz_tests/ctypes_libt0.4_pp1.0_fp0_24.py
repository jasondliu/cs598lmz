import ctypes
ctypes.windll.user32.MessageBoxA(0, "Hello", "Title", 1)

# 파이썬 내장 함수
import time
time.sleep(3)

# 외장 함수
import random
print(random.random())

# 사용자 정의 함수
def my_sum(x, y):
    return x + y

print(my_sum(1, 2))

# 매개변수가 없는 함수
def say():
    return 'Hi'

print(say())

# 매개변수가 여러개인 함수
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum_many(1, 2, 3))
