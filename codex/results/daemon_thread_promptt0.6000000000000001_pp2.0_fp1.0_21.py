import threading
# Test threading daemon

def t_function(name):
    print("Thread %s started" % (name))
    time.sleep(5)
    print("Thread %s ended" % (name))

def main():
    t = threading.Thread(target=t_function, args=("1",), daemon=True)
    t.start()
    print("Thread %s started" % (t.name))
    time.sleep(2)
    print("End of main")

main()

print("All done")

# Test threading daemon

def t_function(name):
    print("Thread %s started" % (name))
    time.sleep(5)
    print("Thread %s ended" % (name))

def main():
    t = threading.Thread(target=t_function, args=("1",), daemon=False)
    t.start()
    print("Thread %s started" % (t.name))
    time.sleep(2)
    print("End of main")

main()

print("All done")
 
# Test threading
