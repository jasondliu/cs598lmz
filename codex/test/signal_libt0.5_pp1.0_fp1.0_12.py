import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def check_if_run(name):
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    for pid in pids:
        try:
            p = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            if name in p:
                return True
        except IOError:
            continue
    return False

def run(name):
    if check_if_run(name):
        return True
    else:
        return False

def check_if_running(name):
    if run(name):
        print("%s is already running" % name)
        sys.exit(0)
    else:
        print("Starting %s" % name)

def stop(name):
    if run(name):
        print("%s is running. Stopping..." % name)
        os.system("pkill -f %s" % name)
