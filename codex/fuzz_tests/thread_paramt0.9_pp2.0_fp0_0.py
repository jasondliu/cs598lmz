import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()
print('main')

#Python에서 쓰레드를 사용해야 하는 경우가 언제일까요?
# 항상 쓰레드를 사용해야 하는 것은 아닙니다. 하지만 만약 여러 쓰레드가 일괄적으로 수행될 때 각각의 쓰레드가 완료 되기 전까지 이후의 작업을 수
