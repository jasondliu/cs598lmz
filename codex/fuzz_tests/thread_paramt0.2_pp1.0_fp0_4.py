import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# 使用生成器函数
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# Create the generator, notice no output appears
c = countdown(3)
print(c)

# Run to first yield and emit a value
print(next(c))

# Run to the next yield
print(next(c))

# Run to next yield
print(next(c))

# Run to next yield (iteration stops)
print(next(c))

# 使用生成器表达式
# 生成器表达式是创建生成器的简单方式，它们的语法跟列表推导式
