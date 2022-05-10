import sys, threading

def run():
    for i in range(10):
        print("Child thread")
   
    print("Child thread id:", threading.get_ident())
    print("Child thread name:", threading.current_thread().getName())


if __name__ == "__main__":
    print("Parent thread name:", threading.current_thread().getName())

    print("Parent thread id:", threading.get_ident())
    print("Parent thread name:", threading.current_thread().getName())

    thread = threading.Thread(target=run)
    thread.start()

    thread.join()
    print("Parent thread")
