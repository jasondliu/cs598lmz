import signal
signal.signal(signal.SIGINT, my_exit)
signal.signal(signal.SIGTERM, my_exit)

try:
    os.chdir(sys.argv[1])
except Exception:
    pass
if os.path.isfile('stop'):
    os.remove('stop')
if os.path.isfile('stopped'):
    os.remove('stopped')

close_fds = True
if sys.platform == 'win32':
    close_fds = False

current_address = tempfile.TemporaryFile()
current_port = None
proc = None

