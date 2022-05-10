import threading
# Test threading daemon.


class File(threading.Thread):
    """
    File class
    """

    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename

    def run(self):
        """
        File Thread run function
        :return:
        """
        for line in open(self.filename, 'r'):
            print(line)


class Worker(threading.Thread):
    """
    Worker class
    """
    def __init__(self, name, count):
        threading.Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        """
        Worker Thread run function
        :return:
        """
        print("Threading {0} started".format(self.name))
        for i in xrange(1, self.count):
            print("Thread {0} value {1}".format(self.name, i))


a = File("file1.txt")
b = File("file2.txt")
a
