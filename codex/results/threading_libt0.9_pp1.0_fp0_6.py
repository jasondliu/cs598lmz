import threading
threading.enumerate()
#[<_MainThread(MainThread, started 11868)>,
# <Thread(Thread-1, started 12312)>,
# <Heartbeat(Thread-2, started daemon 12320)>, 
# <HistorySavingThread(IPythonHistorySavingThread, started 12328)>,
# <ParentPollerWindows(Thread-3, started daemon 12576)>]
```

```
import threading
threading.currentThread()
#<_MainThread(MainThread, started 11868)>
```

* создать и запустить поток можно так

```
import threading
thread1 = threading.Thread(target=task, args=(10,))
thread1.start()
```

* главный поток не дожидается выполнения потока и
