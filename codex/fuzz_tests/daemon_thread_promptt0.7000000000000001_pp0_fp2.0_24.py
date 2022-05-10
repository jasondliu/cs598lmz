import threading
# Test threading daemon
def run(name):
    print("[+] Thread %s is running..." %name)
    time.sleep(2)
    print("[+] Thread %s is done..." %name)
th=threading.Thread(target=run, name='th', args=('th',))
th.setDaemon(True)
th.start()
print('[+] main thread is done')
