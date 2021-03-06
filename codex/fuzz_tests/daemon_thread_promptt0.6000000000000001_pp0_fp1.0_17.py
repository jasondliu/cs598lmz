import threading
# Test threading daemon
# https://stackoverflow.com/questions/1191374/using-module-subprocess-with-timeout

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print ('Thread started')
            self.process = subprocess.Popen(self.cmd, shell=True)
            #self.process.communicate()
            print ('Thread finished')

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print ('Terminating process')
            self.process.terminate()
            thread.join()
        print (self.process.returncode)

#cmd = Command("sleep 2")
cmd = Command("sleep 2 && ls -la")
cmd.run(timeout=3)
