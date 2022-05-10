import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# your script starts here

import time

time.sleep(1)
print('2')

time.sleep(1)
print('3')

time.sleep(1)
print('Done')
```

```shell
$ node script.js | node proxy.js
2
3
Done
```
