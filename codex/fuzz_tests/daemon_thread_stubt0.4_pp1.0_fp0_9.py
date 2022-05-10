import sys, threading

def run():
    print('Hello')
    sys.exit()

thread = threading.Thread(target=run)
thread.start()
thread.join()
print('World')

# Hello
# World

# 使用join()方法，主线程会等待子线程结束后才继续运行，
# 主线程会等待子线程结束后才继续运行，这样就可以把线程当做守护线程来使用。

# 使用threading模块创建线程，主线程退出后，子线程kill掉，
#
