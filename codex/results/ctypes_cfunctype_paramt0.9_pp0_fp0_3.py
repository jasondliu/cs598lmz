import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)

def thread_func(v, msg):
    print ('%i -&gt; %s' % (v, msg))

fn = FUNTYPE(thread_func)

for i in range(5):
    ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), fn)
</code>
And the output is this:
<code>6928 -&gt; None
</code>
It seems that the value of <code>thread.ident</code> changes every time, is it possible to work around it?
PS
I understand that in this case I should use Lock and <code>thread.join</code> but I can't because if a different function is called in the thread the program should not wait until it finishes.


A:

<blockquote>
<p>It seems that the value of <code>&lt;code&gt;thread.ident&lt;/code&gt;</code> changes every time, is it possible to work around it?
