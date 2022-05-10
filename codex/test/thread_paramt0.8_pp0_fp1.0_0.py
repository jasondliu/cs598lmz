import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

for i in range(8):
	print(i)
sys.stdin.read(1)
print('exit')
