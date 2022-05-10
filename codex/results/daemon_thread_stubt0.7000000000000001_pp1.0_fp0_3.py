import sys, threading

def run():
    while True:
        if threading.activeCount() < 250:
            threading.Thread(target=thread).start()

def thread():
    try:
        r = requests.get("http://www.google.com")
    except:
        sys.exit(0)


threading.Thread(target=run).start()
