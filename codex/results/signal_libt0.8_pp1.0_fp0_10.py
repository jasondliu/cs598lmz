import signal
signal.signal(signal.SIGINT, handler)

while True:
    time.sleep(.2)
    print("foo")
</code>
Here is the output of <code>strace</code> on the Python script:
<code>$ strace -p 12352 -p 12353
strace: Process 12353 attached
strace: Process 12352 attached
[...]
[pid 12352] rt_sigprocmask(SIG_BLOCK, [INT], NULL, 8) = 0
[pid 12352] rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
[pid 12352] rt_sigprocmask(SIG_BLOCK, [INT], NULL, 8) = 0
[pid 12352] rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
[pid 12352] rt_sigprocmask(SIG_BLOCK, [INT], NULL, 8) = 0
[pid 12352] rt_sigprocmask(
