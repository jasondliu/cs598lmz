import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class TimeoutException(Exception):
    pass


class Alarm(threading.Thread):
    def __init__(self, sec):
        self.sec = sec
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.sec)
        raise TimeoutException("Running too Long")


def calculate_password(door_id, counter=0):
    password = ''
    while len(password) < LENGTH:
        try:
            m = hashlib.md5()
            m.update(door_id + str(counter))
            digest = m.hexdigest()
            if digest.startswith('00000'):
                print "Found match %s" % digest
                password += digest[5]
            counter += 1
        except TimeoutException:
            print "Timeout"
            break

    print "DONE"
    print password
    return password


def file_get_contents(filename):
    with open(filename
