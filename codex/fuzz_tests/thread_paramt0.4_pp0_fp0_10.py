import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()

# output:
# main
# thread
```

```py
# 这个例子中，主线程在子线程启动前结束，因此子线程永远得不到运行的机会。
import threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()
sys.stdout.write('main\n')

# output:
# main
```

```py
# 这个例子中，主线程在子线程启动前结束，因此子线程永远得不到运行的机会。
import threading
threading.Thread(target=lambda:
