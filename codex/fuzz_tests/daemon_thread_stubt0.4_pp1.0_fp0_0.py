import sys, threading

def run():
    print("Thread {} starting".format(threading.get_ident()))
    for i in range(1, 100000):
        print("Thread {}: count={}".format(threading.get_ident(), i))

if __name__ == "__main__":
    print("Thread {} starting".format(threading.get_ident()))
    for i in range(5):
        thread = threading.Thread(target=run)
        thread.start()
        print("Thread {} started".format(thread.ident))
    print("Thread {} finishing".format(threading.get_ident()))
