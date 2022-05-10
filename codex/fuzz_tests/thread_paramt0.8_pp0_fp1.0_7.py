import sys, threading
threading.Thread(target=lambda: sys.stdout.read(1)).start()   # Don't let the readline block return before the client is calling
</code>

Or, use the <code>subprocess</code> module's <code>Popen</code> class, which has the convenient <code>communicate</code> method.
Test program:
<code>import subprocess

command = "cat"

p = subprocess.Popen(command, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Send some input
p.stdin.write("Foo\n")
p.stdin.write("Bar\n")

# Send EOF
p.stdin.flush()
p.stdin.close()

while True:
    line = p.stderr.readline()
    if line == "":
        break

    print repr(line)
</code>
Here, the program creates a pipe for each of stdout, stdin and stderr, then uses those pipes to communicate
