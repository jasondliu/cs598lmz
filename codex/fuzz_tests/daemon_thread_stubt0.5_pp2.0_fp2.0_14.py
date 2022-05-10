import sys, threading

def run():
    print("Thread started.")
    time.sleep(10)
    print("Thread finished.")

def main():
    print("Main started.")
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("Main finished.")

if __name__ == "__main__":
    main()
