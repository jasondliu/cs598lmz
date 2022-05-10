import sys, threading

def run():
    data = []
    for i in range(0, 100):
        data.append("1234567890"*4)
    for i in range(0, 100):
        io.write("5678")
    sys.exit(0)

io = ChildIO()
t = threading.Thread(target=run)
t.start()
d = io.read(4096)
io.flush()
print("finished")
print("read", d)
