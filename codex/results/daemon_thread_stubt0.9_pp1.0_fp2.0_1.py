import sys, threading

def run():
    from nose import run
    from . import sniff

    sys.argv = ['nose']
    run(mod=sniff)

thread = threading.Thread(target=run)
thread.start()
thread.join()
</code>
Both lines:
<code>thread = threading.Thread(target=run)
thread.start()
</code>
are run at import time (at the end of the file). 
You might find some tips with this SO question. 

