import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("World")
        time.sleep(1)

if __name__ == "__main__":
    main()
</code>
I want to be able to run the <code>run()</code> function in a separate thread, but I also want to be able to run the <code>main()</code> function in the main thread.
I have tried using <code>thread.join()</code> in the <code>main()</code> function, but it doesn't work.
I have also tried using <code>thread.daemon = True</code> in the <code>main()</code> function, but it doesn't work either.
I have also tried using <code>sys.exit()</code> in the <code>main()</code> function, but it doesn't work either.
I have also tried using <code>thread.exit()</code> in the <code>main
