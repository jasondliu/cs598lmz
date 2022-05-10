import threading
# Test threading daemon

def myfunc():
    print("Start myfunc")
    time.sleep(5)
    print("End myfunc")

if __name__ == "__main__":
    print("Start main")
    t = threading.Thread(target=myfunc)
    t.setDaemon(True)
    t.start()
    print("End main")

# End code for threading daemon

#Test threading with subprocess

def myfunc2():
    print("Start myfunc2")
    time.sleep(5)
    print("End myfunc2")

def myfunc1():
    print("Start myfunc1")
    p = subprocess.Popen(["python", "subprocess.py"])
    p.wait()
    print("End myfunc1")

if __name__ == "__main__":
    print("Start main")
    t1 = threading.Thread(target=myfunc1)
    t1.start()
    t2 = threading.Thread(target=myfunc2)
    t2.start()
    print
