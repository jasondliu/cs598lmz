import sys, threading

def run():
	print("Popen run")
	cmd = 'python3.3 ./test1.py'
	p = subprocess.Popen(cmd, shell = True)
	returncode = p.poll()
	print("returncode=%d" % (returncode))
def main():
	run()
	while True:
		time.sleep(1)
		print("main")
if __name__ == "__main__":
	main()
