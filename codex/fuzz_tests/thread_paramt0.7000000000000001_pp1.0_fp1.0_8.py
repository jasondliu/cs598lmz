import sys, threading
threading.Thread(target=lambda: sys.stdout.write('3')).start()
import time
time.sleep(2)
print('2')

# # 4
# Почему не работает? Решение найти!
# from threading import Thread
#
#
# def foo(l, i):
#     l.acquire()
#     print('Hello world! I\'m number %s' % i)
#     l.release()
#
#
# lock = Lock()
#
# for i in range(10):
#     Thread(target=foo, args=(lock, i)).start()


# # 5
# Реализовать скрипт парсинга курса с сайта НБУ (http://www.bank.gov.ua/control/uk/curmetal/detail/currency?period=daily)
# На
