import threading
# Test threading daemon
class TestThreading(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            time.sleep(1)
            print("TestThreading")
# Main function
def main():
    TestThreading()
    while True:
        time.sleep(1)
        print("Main")
if __name__ == '__main__':
    main()
</code>
Output:
<code>Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
</code>
I expect the output to be:
<code>Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
Main
TestThreading
