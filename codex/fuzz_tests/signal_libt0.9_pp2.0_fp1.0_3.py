import signal
signal.signal(signal.SIGINT, signal.default_int_handler)

def pickle_open(base):
    try:
        with open(base + '.pickle', 'wb') as f:
            pickle.dump((base + '.dat', base + '.headers'), f)
    except KeyboardInterrupt:
        pass
    except:
        raise
    try:
        os.remove(base + '.dat')
        os.remove(base + '.headers')
    except OSError:
        pass
    return

def pickle_read(base):
    filename = base + '.pickle'
    rtn = None
    with open(filename, 'rb') as f:
        rtn = pickle.load(f)
    os.remove(filename)
    return rtn


def run_tcpdump(host, base):
    if host:
        args = ['tcpdump', '-i', 'any', '-s', '0', \
        '-w', base + '.dat', host]
    else:
        args = ['t
