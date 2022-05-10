import sys, threading
threading.Thread(target=lambda: sys.stdout.write('My result\n')).start()
</code>
Получаем ожидаемый результат:
<code>$ python3 test.py
My result
</code>
Вероятно, в вашем случае нужно <code>Thread(target=lambda: sys.stdout.write(sql + '\n')).start()</code>.

