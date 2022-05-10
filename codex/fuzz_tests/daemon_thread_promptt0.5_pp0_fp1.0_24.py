import threading
# Test threading daemon
# http://stackoverflow.com/questions/19078170/python-threading-daemon-vs-none
# http://stackoverflow.com/questions/19078170/python-threading-daemon-vs-none

def f(name):
    print("Hello",name)
    time.sleep(3)
    print("Good bye",name)

def main():
    t1 = threading.Thread(target=f, args=("Bob",))
    t2 = threading.Thread(target=f, args=("Alice",))
    t1.start()
    t2.start()
    print("hello main")
    t1.join()
    t2.join()
    print("good bye main")

if __name__ == "__main__":
    main()
