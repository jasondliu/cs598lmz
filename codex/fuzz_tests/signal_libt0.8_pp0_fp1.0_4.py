import signal
signal.signal(signal.SIGTERM, lambda a,b: sys.exit(0))
signal.signal(signal.SIGINT, lambda a,b: sys.exit(0))

def shutdown():
    global running
    running = False

def check_up(host, port, check_name, client_timeout, check_timeout, can_fail=False, env_check=None):
    if env_check:
        if os.getenv(env_check):
            return 0
        else:
            return 1

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(client_timeout)
        s.connect((host, port))
    except IOError:
        return 1

    poller = zmq.Poller()
    poller.register(s, zmq.POLLIN)

    # send the check name
    s.send(check_name)
    if poller.poll(timeout=check_timeout*1000):
        if s.recv
