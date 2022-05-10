import threading
threading.stack_size(67108864)  # 64MB stack
thread = threading.Thread(target = do_something)
thread.start()
thread.join()

print('thread finished...')
print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())


def background():
    import time
    time.sleep(2)
    print('Thread:', threading.current_thread().name)

def worker():
    print('Thread:', threading.current_thread().name)
    t = threading.Thread(target=background)
    t.start()

def main():
    print('Thread:', threading.current_thread().name)
    t = threading.Thread(target=worker)
    t.start()

main()



import threading
import time
import requests

def get_html(url):
    resp = requests.get(url)
    time.sleep(1)
    print(threading.current_thread().name)
    print(resp.text[:
