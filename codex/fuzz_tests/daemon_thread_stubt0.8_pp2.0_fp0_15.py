import sys, threading

def run():
    os.chdir('/mnt/E/Github')
    os.system('sudo nohup python3 Main.py > ~/Desktop/nohup.out &')

try:
    threading.Thread(target=run).start()
except:
    print("Error: unable to start thread")

while True:
    time.sleep(1)
