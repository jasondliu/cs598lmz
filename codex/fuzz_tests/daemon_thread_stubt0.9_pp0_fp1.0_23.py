import sys, threading

def run():
	while True:
		sys.stdout.write('*')
		sys.stdout.flush()

if __name__ == '__main__':
	print(sys.argv)
	# 列表解析
	print([x for x in sys.argv])

	# run()
	threading.Thread(target=run).start()

	print('是你昨晚一个人吗？')
