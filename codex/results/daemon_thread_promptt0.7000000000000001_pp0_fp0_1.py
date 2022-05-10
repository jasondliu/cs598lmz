import threading
# Test threading daemon

def f():
    print("hello")
    for i in range(10):
        print("i", i)
        time.sleep(0.1)

thread = threading.Thread(target=f)
thread.daemon = True
thread.start()

print("thread started")

time.sleep(1)
print("ending")

threading.Thread(target=f)

# Test subprocess output

import subprocess

proc = subprocess.Popen(
    ['ping', '-c', '4', 'google.com'],
    stdout=subprocess.PIPE)

for line in proc.stdout:
    print(line.decode('utf-8').rstrip())

proc.wait()

# Test subprocess output

import subprocess

proc = subprocess.Popen(
    ['ping', '-c', '4', 'google.com'],
    stdout=subprocess.PIPE)

for line in proc.stdout:
    print(line.decode('utf-8').rstrip())
