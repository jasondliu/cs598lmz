import sys, threading
threading.Thread(target=lambda: sys.stderr.write("Line\n")).start()
</code>
The output will look like:
<code>$ time \
&gt;   python3 -c 'import sys, threading; \
&gt;              threading.Thread(target=lambda: sys.stderr.write("Line\n")).start()' \
&gt;   &gt;&gt; /dev/null &amp;
[1] 1428
$ Line
[1]+  Done                    python3 -c 'import sys, threading; \
&gt;                             threading.Thread(target=lambda: sys.stderr.write("Line\n")).start()' &gt;&gt; /dev/null

real    0m0.020s
user    0m0.004s
sys     0m0.000s
$ 
</code>
It takes 20ms to write to stderr in this case.

