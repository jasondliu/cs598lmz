import sys, threading

def run():
	threading.Thread(target = lambda: os.system('python svr.py')).start()
	threading.Thread(target = lambda: os.system('python cln.py')).start()

if __name__ == '__main__':
	run()
