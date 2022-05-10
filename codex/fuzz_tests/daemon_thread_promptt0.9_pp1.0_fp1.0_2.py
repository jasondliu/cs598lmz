import threading
# Test threading daemon
# Run python3 daemon_test1.py to test 
t = threading.Thread(target=Printer.test1, args=None, daemon=True)
t.start()
print(t.isDaemon())
time.sleep(1)
print('done')
