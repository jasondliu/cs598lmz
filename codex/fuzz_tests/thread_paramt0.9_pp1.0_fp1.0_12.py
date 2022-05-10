import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello world\n"),
                daemon=True).start()
time.sleep(2) # wait the thread to f
