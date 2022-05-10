import sys, threading
threading.Thread(target=lambda: sys.stdout.write(str(pow(*map(int,input().split())))))

# by lkz
import sys,threading
t=threading.Thread(target=sys.stdout.write,args=map(str,(pow(*map(int,input().split())),"\n")))
t.start()

# by zyxel0
import sys, threading
x, y, z = map(int, input().split())
t = threading.Thread(target=sys.stdout.write, args=(str(x ** y % z),))
t.start()

# by Muntasir_Roy
import sys, threading
threading.Thread(target=lambda: sys.stdout.write(str(pow(*map(int, input().split()))))).start()

# by frederik
import sys, threading
threading.Thread(target=sys.stdout.write, args=map(str,(pow(*map(int, input().split())), "\n"))).start()

# by lkh
