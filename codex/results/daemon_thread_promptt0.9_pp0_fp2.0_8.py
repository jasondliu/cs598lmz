import threading
# Test threading daemon seting

def t_function(string):
    print("hello from func",string)

for i in range(100):
    t = threading.Thread(target=t_function,args=(i,))
    t.setDaemon(True)
    t.start()

t_function("main process")
