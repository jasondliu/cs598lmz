import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html
# https://pymotw.com/3/threading/
# https://stackoverflow.com/questions/16672978/python-threading-is-daemon-vs-daemon-attribute
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-join
# https://stackoverflow.com/questions/6920302/understanding-pythons-threading-module

# https://stackoverflow.com/questions/15525991/creating-a-daemon-thread-with-python
# https://www.ibm.com/developerworks/aix/library/au-threadingpython/
class DaemonThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        print('DaemonThread.__init__')

    def run(self):
        print('DaemonThread.run')
        while
