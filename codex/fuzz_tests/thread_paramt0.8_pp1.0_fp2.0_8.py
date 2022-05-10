import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Threading\n')).start()

- 파이썬은 프로그램이 끝날 때 까지 기다린다. 
- 다루고 있는 데이터가 많은 경우에는 시간이 오래 걸린다.
- 그렇기에 위와 같이 스레드를 생성하여 동시에 작업을 수행하면 자원을 최소화 할 수 있다.

```

