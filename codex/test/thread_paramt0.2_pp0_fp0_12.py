import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# 使用生成器函数让调用方控制何时处理数据
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = 'Four score and seven years ago...'
result = list(index_words_iter(address))
print(result[:3])

# 生成器函数的另一个优点是它们可以被用作协程
def print_matches(matchtext):
    print('Looking for', matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)

# Example use
