import sys, threading

def run():
    for i in range(10):
        print('child', i)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('main thread')

# child 0
# child 1
# child 2
# child 3
# child 4
# child 5
# child 6
# child 7
# child 8
# child 9
# main thread

# 函数run()的执行是在线程t中进行的，它的返回值直接被丢弃了，
# 但是可以在run()函数中使用全局变量

# 如果要获取子线程的返回值，可以在创建Thread对象时，
#
