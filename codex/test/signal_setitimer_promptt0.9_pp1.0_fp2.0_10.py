import signal
# Test signal.setitimer(ITIMER_PROF, x)


def signal_prof_state(sig):
    args = signal.setitimer(signal.ITIMER_PROF, 0)
    signal.setitimer(signal.ITIMER_PROF, args)
    return args
state = signal_prof_state(SIGALRM)
if state[0] != 0 or state[1] != 0:
    print("already in use")


def signal_reset_prof_state():
    if state[0] != 0 or state[1] != 0:
        signal.setitimer(signal.ITIMER_PROF, state)


signal_reset_prof_state()
SIGNAL_DEFAULT = object()
SIGNAL_IGNORE = object()
SIGNAL_TRAMPOLINE = object()
SIGNAL_CALLBACK = object()


def register_at_fork_across_implementations(callback, copy, prep):
    try:
        from multiprocessing import set_for_test
    except ImportError:
        pass
