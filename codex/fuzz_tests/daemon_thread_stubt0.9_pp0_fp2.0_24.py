import sys, threading

def run():
    sys.modules['_thread'].start_new_thread = start_new_thread
    sys.modules['_thread'].allocate_lock = allocate_lock

def start_new_thread(func, args):
    func(*args)

def allocate_lock():
    return threading.RLock()
</code>
it should be used as:
<code>from fake_threads import run

run()
# ... your code
</code>
I have tested this with <code>smtplib</code> (<code>smtplib.SMTP</code>), and it worked just like before.

