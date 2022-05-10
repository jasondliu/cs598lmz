import sys, threading

def run():
    for i in range(10):
        print 'thread:', i
    return

t = threading.Thread(target=run)
t.start()

sys.exit()  # 这行代码会将主线程退出, 从而导致子线程终止

for i in range(10):
    print 'main:', i

#out:
# thread: 0
# main: 0
# thread: 1
# main: 1
# thread: 2
# main: 2
# thread: 3
# main: 3
# thread: 4
# main: 4
# thread: 5
# main: 5
# thread: 6
# main: 6
# thread: 7
# main: 7
# thread: 8
# main: 8
# thread: 9
# main: 9
#
# Process finished with exit code 0

# 可以看到, 通过sys.exit(), 主线程
