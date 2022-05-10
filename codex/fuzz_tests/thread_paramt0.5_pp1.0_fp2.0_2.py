import sys, threading
threading.Thread(target=lambda:sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda:sys.stdout.write('Hello from Thread 2\n')).start()
</code>
Результат:
<code>Hello from Thread 1
Hello from Thread 2
</code>

