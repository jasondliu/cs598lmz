import ctypes
# Test ctypes.CFUNCTYPE()
def b(x):
	y = raw_input("name:")
	print y + ' ' + str(x)

a=ctypes.CFUNCTYPE(None,ctypes.c_void_p)(b)
a(3)
#
#import atexit
#
#atexit.register(lambda x:subprocess.check_call([sys.executable, '-c', "import os; os.system('zsh')"]), 'goodbye')
#subprocess.check_call([sys.executable, '-c', "import os; os.system('uname -a')"])




#print 'hahah'
# make sure the mainloop is removed
#del zsh_mainloop
#subprocess.call([sys.executable, '-c', 'import os; os.system(sys.argv[1])', 'echo hello from python'])
