import sys, threading

def run():
	args = ""
	for i in sys.argv:
		if i == "--debug":
			i = "--nodaemon --debug"
		args = args + " " + i
	cmd = "python main.py" + args
	os.popen(cmd)

def start():
	print "starting..."
	os.chdir("./bin")
	t = threading.Thread(target = run)
	t.start()
	print "started..."

def stop():
	print "stopping..."
	os.popen("ps -ef | grep python | grep 'main.py --daemon' | awk '{print $2}' | xargs kill -9")
	print "stopped"

def reload():
	print "reloading..."
	stop()
	print "waiting for 10s for the server to shutdown..."
	time.sleep(10)
	start()
	print "reloaded..."

def clean():
	print "cleaning..."
	os.system("rm -r ./bin/cache/")
	
