import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read()),daemon=True).start() # thread for printing

while True:
	if b'x' not in ser.read():
		print('HELP')
		time.sleep(2)
### END
