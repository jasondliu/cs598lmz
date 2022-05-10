import threading
# Test threading daemon mode
class TestThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            t = time.strftime('%H:%M:%S', time.localtime())
            print t
            time.sleep(1)
TestThread()

# Test subprocess
# proc = subprocess.Popen('ping -c 1 192.168.10.1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print proc.stdout.read()
# print proc.stderr.read()
# print 'Return code: %d' % proc.returncode

# Test os.listdir
# print os.listdir('/home/lixuze')
# print os.path.exists('/home/lixuze/test.txt')
# print os.path.isfile('/home/lixuze/test.txt')

