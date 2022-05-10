import threading
threading.stack_size(67108864)

def main():
    print("Hello World!")

thread = threading.Thread(target=main)
thread.start()
</code>
I'm using Python 3.6.5.

