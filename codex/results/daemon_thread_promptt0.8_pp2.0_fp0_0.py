import threading
# Test threading daemon.
if __name__ == "__main__":
    print("Main Thread START")

    class MyThread(threading.Thread):
        def run(self):
            print(self.name + " START")
            for i in range(3):
                print(self.name + " " + str(i))
            print(self.name + " END")

    t = MyThread(name="Worker")
    t.daemon = True
    t.start()
    print("Main Thread END")
