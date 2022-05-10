import sys, threading

def run():
  if (sys.platform.startswith("win")):
    subprocess.Popen("ml.bat", shell=True)
  elif (sys.platform.startswith("mac")):
    subprocess.Popen("ml.sh", shell=True)
  else:
    subprocess.Popen("ml.sh", shell=True)

threads = []
for i in range(1):
  thread = threading.Thread(target=run)
  threads.append(thread)
  thread.start()
