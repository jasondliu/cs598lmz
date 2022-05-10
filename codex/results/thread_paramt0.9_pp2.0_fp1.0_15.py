import sys, threading
threading.Thread(target=lambda:sys.stdout.write(input())).start()
</code>
One could use the <code>run_in_executor</code> method of the threading event loop, though this isn't necessarily easy for general usage in a REPL, and might not be desired for a script:
<code>import sys, asyncio
asyncio.get_event_loop().run_in_executor(None,
    lambda:sys.stdout.write(input()))
</code>
The above code is asynchronous, and works in either Python 3.7+ or 3.6+ with <code>asyncio</code> backported.  See <code>asyncio</code> docs on thread executors
A REPL could be written to make the above easy to use, e.g.:
<code>async def future_input(message, *etc, **kw):
    return (await asyncio.get_event_loop().run_in_executor(None,
        lambda:input(message))
</code>
Or at least a function to wrap arbitrary code in a thread:
<code>def run_thread
