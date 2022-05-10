import sys, threading

def run():
    os.system("python cam_gui.py")

threading.Thread(target=run).start()
