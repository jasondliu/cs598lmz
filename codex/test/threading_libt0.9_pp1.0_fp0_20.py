import threading
threading.Thread(target=main).start()

# This method is useful if your main thread halts but you still want the process to terminate.
def idle():
    while True:
        time.sleep(1)

threading.Thread(target=idle).start()
