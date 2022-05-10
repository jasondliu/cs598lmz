import threading
threading.stack_size(67108864)

def main():
    print("Hello World!")

thread = threading.Thread(target=main)
thread.start()
