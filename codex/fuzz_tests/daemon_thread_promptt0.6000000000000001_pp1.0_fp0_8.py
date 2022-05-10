import threading
# Test threading daemon
def thread_test():
	print('start')
	time.sleep(10)
	print('end')

for i in range(5):
	t = threading.Thread(target=thread_test)
	t.setDaemon(True)
	t.start()

print('main thread end')

# 运行结果：
# start
# start
# start
# start
# start
# main thread end

# 当主线程退出的时候，子线程kill掉
