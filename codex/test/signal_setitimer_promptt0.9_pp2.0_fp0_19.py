import signal
# Test signal.setitimer() function
# This function is only available on UNIX
setitimer = getattr(signal, "setitimer", None)
if setitimer is not None:
    funcname = "setitimer"
    func_args = []
    func_return = []
    def cleanup(sig, frame):
        pass

    sig = signal.SIGALRM
    pre_value = 5000

    print('*** Testing %s ***' % funcname)
