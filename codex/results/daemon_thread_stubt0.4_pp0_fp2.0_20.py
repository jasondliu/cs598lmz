import sys, threading

def run():
    print("Thread started")
    try:
        import main
        main.main()
    except Exception as e:
        print("Error running main:", e)
    finally:
        print("Thread exiting")

def main():
    print("Starting thread")
    thread = threading.Thread(target=run)
    thread.start()
    print("Thread started")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping thread")
        thread.join()
        print("Thread stopped")

if __name__ == "__main__":
    main()
