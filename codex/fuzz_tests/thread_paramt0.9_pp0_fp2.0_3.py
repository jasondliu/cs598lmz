import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input() + "\n")).start()
</code>
Can also be written as:
<code>Thread(target=lambda: write(input() + "\n")).start()
</code>
Just for completeness, the equivalent in C# (Requires .NET Core) is:
<code>using System.Diagnostics;
using System.Threading;
using static System.Console;

static void Main(string[] args) {
    bool done = false;
    new Thread(() =&gt; { while (!done) WriteLine(ReadLine()); }).Start();

    Stopwatch time = Stopwatch.StartNew();
    while (time.ElapsedMilliseconds &lt; 10_000) {
        Thread.Sleep(10);
    }
    done = true;
} 
</code>
Python 3.2+
A seperate thread is unnecessary in recent versions of Python (3.2+).
<code>from sys import stdout
from subprocess import Popen, PIPE
from time import sleep

p = Popen('python -u input.
