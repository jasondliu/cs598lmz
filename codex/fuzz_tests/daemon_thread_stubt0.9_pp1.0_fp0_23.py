import sys, threading

def run():
	while True:
		try:
			line = input()
			if line == 'END':
				break
			prefix = 'master: ' if line.strip()[:1] == '>' else ''

			print(prefix + line.strip())
		except:
			break
	print('END')

sys.stdout = sys.stderr = open(os.devnull, 'w')
threading.Thread(None, run, 'master').start()
