import sys, threading

def run():
    str_cmd = sys.argv[1]
    output = commands.getoutput(str_cmd)
    print output

try:
	run()
except Exception, e:
	print str(e)
