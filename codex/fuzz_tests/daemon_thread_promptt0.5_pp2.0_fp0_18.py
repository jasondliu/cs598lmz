import threading
# Test threading daemon
import time


class TestDaemon(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))
        time.sleep(1)
        print("{} finished!".format(self.getName()))


if __name__ == "__main__":
    d = TestDaemon(name="Daemon")
    d.setDaemon(True)
    d.start()
    d.join()
    print("d.isAlive() = {}".format(d.isAlive()))
    print("Exiting...")
