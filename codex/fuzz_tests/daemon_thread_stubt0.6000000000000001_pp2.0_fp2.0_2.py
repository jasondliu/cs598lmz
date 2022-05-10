import sys, threading

def run():
	global v
	print(v)
	v = 0

v = 1
t = threading.Thread(target=run)
t.start()
while t.is_alive():
	print(v)
	v = 2
print(v)
