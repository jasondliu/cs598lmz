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

while not os.path.isfile('stop'):
    try:
        if proc and proc.poll() is not None:
            proc = None
            if os.path.isfile('stopped'):
                sys.exit()
            current_port = None
            current_address = tempfile.TemporaryFile()

        if not proc:
            socket.create_connection(('www.google.com', 80))
            current_address =
