import sys, threading

def run():
	print("Starting: %s" % sys.argv[1])
	subprocess.run("cd / && python /home/ec2-user/production/app.py", shell=True)

try:
	thread_count = int(sys.argv[2])
except:
	thread_count = 1

threads = [threading.Thread(target=run) for x in range(thread_count)]
for thread in threads:
	thread.start()
for thread in threads:
	thread.join()
