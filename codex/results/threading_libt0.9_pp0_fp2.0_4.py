import threading
threading.current_thread()
#<_MainThread(MainThread, started 3552)>

import threading
# semaphore - 기준점
# semaphore 지정하면 스레드 생성 개수 제한 가능
s = threading.Semaphore(10)
s.get_value() # 10
for i in range(20):
    t = threading.Thread(target=consume)
    t.start()
