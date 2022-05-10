import threading
# Test threading daemon
t = threading.Thread(name='non-daemon', target=do_this, args=('non-daemon', 5))

t.start()

t = threading.Thread(name='daemon', target=do_this, args=('daemon', 5), daemon=True)

t.start()

t = threading.Thread(name='non-daemon', target=do_this, args=('non-daemon', 5))

t.start()

t = threading.Thread(name='daemon', target=do_this, args=('daemon', 5), daemon=True)

t.start()
