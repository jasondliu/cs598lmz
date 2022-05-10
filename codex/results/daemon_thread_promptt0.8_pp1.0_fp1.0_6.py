import threading
# Test threading daemon
class mythread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I am " + self.name + ' @ ' + str(i)
            print(msg)
if __name__ == '__main__':
    t = mythread()
    t.setDaemon(True)
    t.start()
    t.join()
    print("Main thread is over")
