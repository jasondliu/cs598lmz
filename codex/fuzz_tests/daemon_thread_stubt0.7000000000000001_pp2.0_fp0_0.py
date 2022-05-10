import sys, threading

def run():
    try:
        os.system("start " + "\"\" \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"")
        sys.exit()
    except:
        pass
    
threading.Timer(10, run).start()
