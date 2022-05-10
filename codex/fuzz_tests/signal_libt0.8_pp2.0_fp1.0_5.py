import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
</code>
The problem with this is that we would have to add this to every file in our project. Is there a way to globally set the signal handler?


A:

<blockquote>
<p>Is there a way to globally set the signal handler?</p>
</blockquote>
The Python interpreter has a function <code>PyOS_setsig(int sig, PyOS_sighandler_t handler)</code> that you can use to register your own signal handler. (The macro <code>PyOS_setsig</code> uses <code>PyOS_sighandler_t</code> as the signature of the signal handler function. For your convenience, it is defined as <code>typedef RETSIGTYPE (*PyOS_sighandler_t)(int);</code>.)
So for example, to register the signal handler for Ctrl + C, you can do the following in the module <code>mysignal.c</code>:
<code>#include &lt;signal.h&gt;

