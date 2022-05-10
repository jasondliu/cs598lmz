import threading
# Test threading daemon

def ziki(x):
    print("I'm ziki, my name is", x)

def kiki(y):
    print("I'm kiki, my name is", y)


if __name__ == "__main__":
    z = threading.Thread(target=ziki, args=("Ziki",))
    z.daemon = False
    k = threading.Thread(target=kiki, args=("Kiki",))
    k.daemon = True
    z.start()
    k.start()

    z.join()
    print("Joined")
