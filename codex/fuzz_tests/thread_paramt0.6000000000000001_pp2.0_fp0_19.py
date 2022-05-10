import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()
threading.Thread(target=lambda: sys.stdout.write('.')).start()
</code>
This is all very well and I can see the two dots being printed in the console.
However, when I do the following:
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()
threading.Thread(target=lambda: sys.stdout.write('.')).start()
sys.stdout.flush()
</code>
I see no output.
I've also tried <code>sys.stdout.flush()</code> in the lambda, and it doesn't work either.
I also tried redirecting to a <code>StringIO</code> and <code>flush()</code> on that and it didn't work.
Am I missing something obvious?
EDIT:
The reason I want to do this is because I'm writing a unit test for some code that does a lot of <code>sys.stdout.write()</code> calls, and I'd like to check that it's written the
