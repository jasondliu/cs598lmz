import sys, threading

def run():
	while True:
		s = input()
		print(s)

threading.Thread(target=run).start()

while True:
	s = input()
	print(s)
