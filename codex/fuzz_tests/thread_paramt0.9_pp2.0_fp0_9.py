import sys, threading
threading.Thread(target=lambda: sys.stdout.write("asd")).start()
</code>
What I would expect to happen is it should just print <code>asd</code> without anything else. That is what I get if the thread prints to <code>stdout</code> without any other characters in the surrounding code, but with the extra characters I get a lot of text like
<code>Thread-12
Thread-11
Thread-14
&lt;omitted&gt;
</code>
Why do I get this output? Is it Python just printing information about the newly started threads, or is it something else?
Furthermore, when I run the same code in IDLE, it works exactly as I would expect it to.


A:

IDLE doesn't have thread support, see https://bugs.python.org/issue12157
The printed text is thread traceback info.

