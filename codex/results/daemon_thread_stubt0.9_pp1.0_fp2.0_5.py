import sys, threading

def run():
	while True:
		cmd = file("loop.command", "r").readline()
		cmd = cmd.strip()
		if cmd == "":
			print "No command!"
			return
		infile = cmd + ".in"
		outfile = cmd + ".out"

		infile = file(infile, "r")
		outfile = file(outfile, "w")
		sys.stdin, sys.stdout = infile, outfile
		print "Running", cmd, ":"
		execfile(cmd + ".py")
		print "Exciting", cmd, ":"
		print
		outfile.close()

try:
	while True:
		threading.Thread(target = run).start()
except: pass
