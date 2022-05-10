import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()
import msvcrt
def wait(msg='Press any key to continue...'):
    print(msg, end=' ')
    msvcrt.getch()
wait()
</code>

