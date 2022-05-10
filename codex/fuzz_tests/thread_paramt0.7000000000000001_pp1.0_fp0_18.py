import sys, threading
threading.Thread(target=lambda: sys.stdout.write("E\n")).start()
threading.Thread(target=lambda: sys.stdout.write("F\n")).start()
sys.stdout.write("A\n")
sys.stdout.write("B\n")
sys.stdout.write("C\n")
sys.stdout.write("D\n")
</code>
The output is:
<code>ABCDE
F
</code>
Because no synchronization is used, the threads "communicate" directly to the standard output (which is synchronized). On the other hand, assume a program like this:
<code>import sys, threading

def run(x):
    sys.stdout.write(str(x) + "\n")

threading.Thread(target=lambda: run("E")).start()
threading.Thread(target=lambda: run("F")).start()
run("A")
run("B")
run("C")
run("D")
</code>
The output can be:
<code>E
A
B
C
D
F

