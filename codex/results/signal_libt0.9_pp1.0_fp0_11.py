import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)

try:
	options, args = getopt.getopt(sys.argv[1:], "U:C:D:O:", ["user", "password", "cache", "descriptor"])
except getopt.GetoptError:
	print sys.exc_info()[1]
	sys.exit(1)

db_user = ""; db_pass = ""; cache_dir = ""; desc_dir = ""

for opt, value in options:
	if opt == "-U":
		db_user = value
	if opt == "-C":
		cache_dir = value
	if opt == "-O":
		desc_dir = value
		
cwd = os.path.dirname(os.path.abspath(__file__))

def mkdir_p(dir):
	if not os.path.isdir(dir):
		os.makedirs(dir)

def cull_old_data(path, max_age = 31):
