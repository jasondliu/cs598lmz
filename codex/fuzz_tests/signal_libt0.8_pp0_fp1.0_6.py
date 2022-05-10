import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) 
##################################################
import os, sys
if os.path.exists(__file__ + '.py'):
	exec(open(__file__ + '.py').read())
else:
	exec(compile(open(__file__ + '.pyw').read(), __file__ + '.pyw', 'exec'))
