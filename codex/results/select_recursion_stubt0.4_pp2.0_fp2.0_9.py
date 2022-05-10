import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [])

def test_select_keyboardinterrupt():
    try:
        select.select([], [], [], 0.1)
    except KeyboardInterrupt:
        pass

def test_select_interrupted_syscall():
    import os
    import errno

    class InterruptedSyscall(OSError):
        pass

    class F:
        def fileno(self):
            raise InterruptedSyscall(errno.EINTR, "interrupted syscall")

    f = F()
    try:
        select.select([f], [], [], 0.1)
    except InterruptedSyscall:
        pass

def test_select_interrupted_syscall_2():
    import os
    import errno

    class InterruptedSyscall(OSError):
        pass

    def interrupted_syscall():
        raise InterruptedSyscall(errno.EINTR, "interrupted syscall")

    select.select(
