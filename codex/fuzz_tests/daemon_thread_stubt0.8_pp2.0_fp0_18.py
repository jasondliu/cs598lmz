import sys, threading

def run():
    sys.stdout.write(name)

if __name__ == "__main__":
    h = []
    for i in range(10):
        name = "Thread #%s\n" % i
        t = threading.Thread(target=run)
        h.append(t)
        t.start()
    print("done")
