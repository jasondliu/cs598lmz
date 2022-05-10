import sys, threading

def run():
    print("Starting the server")
    server = Server()
    server.run()

def test():
    print("Starting the test")
    test = Test()
    test.run()

threads = []
t = threading.Thread(target=run)
t.start()
threads.append(t)

t = threading.Thread(target=test)
t.start()
threads.append(t)

for t in threads:
    t.join()
