import sys, threading

def run():
	sys.stdout.write("\n")
	sys.stdout.flush()

threading.Timer(1, run).start()

def main():
	win = 0
	loss = 0

	sys.stdout.write("\n" * 100)
	sys.stdout.flush()

	while True:
		try:
			if random.random() > 0.5:
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K")
				sys.stdout.write("Won!\n")
				sys.stdout.flush()
				win += 1
			else:
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K")
				sys.stdout.write("Loss!\n")
				sys.stdout.flush()
				loss += 1
			sys.stdout.
