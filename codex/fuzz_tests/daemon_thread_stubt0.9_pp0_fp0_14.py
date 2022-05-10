import sys, threading

def run():
    os.system("python3 server.py &")
    time.sleep(1)
    os.system("python3 client.py")

thread = threading.Thread(target=run)
thread.start()
