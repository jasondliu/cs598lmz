import sys, threading

def run():
	c = sys.stdin.read(1)
	sys.stdout.write(c)
	sys.stdout.flush()

sys.stdout.write('*')
sys.stdout.flush()

while True:
	threading.Thread(target=run).start()
