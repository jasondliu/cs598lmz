import threading
# Test threading daemon

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()


</code>
Как сделать чтобы скрипт завершался  только после запуска всех потоков? То есть после вывода слова "Worker" 5  раз, а не после первого вывода.  

