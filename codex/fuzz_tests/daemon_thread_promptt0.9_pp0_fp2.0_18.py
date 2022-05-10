import threading
# Test threading daemon mode
def run():
    print("listen")
    time.sleep(2)
    print("listen again")
    time.sleep(2)

t=threading.Thread(target=run)
t.start()
print("go")
t.join()
print("go again")
t.dameon=True
