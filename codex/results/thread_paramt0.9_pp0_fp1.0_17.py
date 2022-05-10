import sys, threading
threading.Thread(target=lambda: sys.stdout.write("a")).start()
</code>
executes in only 2 seconds on pypy, 10 seconds on the original Python,
and even slower on the Cythoned Python-2.7.10. The two threads create a deadlock by both holding the GIL and want to write to stdout before they release it.
For Cython-compiled version it is then strange to see that when replacing
<code>output1 = np.zeros((3, 3))
output2 = np.zeros((3, 3))
</code>
by
<code>output1 = np.zeros((3, 3, 10))
output2 = np.zeros((3, 3, 10))
</code>
the time goes up 5x from 0.07 s to 0.5 s. That is, as a consequence of creating bigger outputs, the loop becomes slower.
I do not think that this makes sense.
Can anyone help?

