import sys, threading

def run():
    print("Starting " + threading.current_thread().name)
    for i in range(10):
        print("Thread " + threading.current_thread().name + " counting " + str(i))
        # time.sleep(1)
    print("Exiting " + threading.current_thread().name)

def main():
    print("Starting " + threading.current_thread().name)
    thread = threading.Thread(name="testThread", target=run)
    thread.start()
    thread.join()
    print("Exiting " + threading.current_thread().name)

if __name__ == "__main__":
    main()
