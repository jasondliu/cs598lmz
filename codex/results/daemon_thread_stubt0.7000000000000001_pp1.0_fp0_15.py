import sys, threading

def run():
	exec(open("%s.py" % sys.argv[1]).read())

t = threading.Thread(target = run)
t.start()

import IPython.Shell
ipshell = IPython.Shell.IPShellEmbed(argv = [])
ipshell()
