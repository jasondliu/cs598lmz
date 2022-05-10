import sys, threading

def run():
    cmd = sys.executable + ' -m pip install --upgrade pip'
    os.system(cmd)
    os.system('pip install -r requirements.txt')

threading.Thread(target=run).start()
