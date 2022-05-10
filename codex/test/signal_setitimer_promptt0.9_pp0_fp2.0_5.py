import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
I_TIMER_VIRTUAL = 2

#----------------------------------------------------------------


class get_id (object):
    """ Used to get the current OS thread ID.
    """

    SYS_gettid = 186

    def get_val(self):
        if self.thread_id is not None:
            return self.thread_id
        try:
            m_gettid = c_long.in_dll(
                ctypes.CDLL("libc.so.6"),
                "syscall").__getitem__(self.SYS_gettid)
        except:
            raise NotImplementedError("thread id is not implemented "
                                      "in this OS")
        VAL_gettid = c_long(0)
        m_gettid(byref(VAL_gettid))
        self.thread_id = VAL_gettid.value
        return self.thread_id

    def __call__(self):
        return self.get_val()

