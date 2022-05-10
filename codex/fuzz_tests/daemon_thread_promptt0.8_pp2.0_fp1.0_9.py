import threading
# Test threading daemonization
t = threading.Thread(target=_wait_and_exit)
t.daemon = True
t.start()

# Test threading subprocess
ps = []
for i in range(0, _count):
    p = subprocess.Popen(["python3", "./dummy-child-process.py"])
    ps.append(p)

for i in range(0, _count):
    ps[i].wait()

# Test threading subprocess with dameon
for i in range(0, _count):
    p = subprocess.Popen(["python3", "./dummy-child-process.py"], daemon=True)
    ps.append(p)

time.sleep(_count)

sys.exit(0)
