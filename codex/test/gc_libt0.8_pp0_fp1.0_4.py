import gc, weakref, functools

def _deref(ref):
    return ref()


def _print_msg(msg):
    if msg.msg_id in ('tty.write', 'tty.write_raw'):
        return msg
    else:
        return msg[:5]+'...'

class CmdQueue:
    def __init__(self, max_history=4096):
        self.history = []
        self.msg = []
        self.max_history = max_history
        self.w = None
        self.status_cb = None
        self.pending_cb = None

    def set_status_cb(self, f):
        self.status_cb = f
        # tell status bar about pending msg
        if f:
            if len(self.msg) > 0:
                f(len(self.msg))

    def set_pending_cb(self, f):
        self.pending_cb = f
        if f:
            f(len(self.msg))

