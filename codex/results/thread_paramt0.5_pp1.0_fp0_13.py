import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# Python 3
import sys
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# Python 2
import sys
threading.Thread(target=lambda: sys.stdout.write(raw_input())).start()
```

##### [9.6.2.2.2.2](https://docs.python.jp/3/library/threading.html#threading.Thread.start)

> このメソッドは、新しいスレッドを開始します。このスレッドは、target の引数に渡された callable を呼び出します。args と kwargs は、callable に渡される引数とキーワード引数です。

> このメソッドは、スレッドが開始されるまで待ちません。開始され
