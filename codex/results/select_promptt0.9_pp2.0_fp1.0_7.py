import select
# Test select.select()

def accepts(*types):
    def check_accepts(f):
        assert len(types) == f.func_code.co_argcount
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), \
                       "arg %r does not match %s" % (a,t)
            return f(*args, **kwds)
        new_f.func_name = f.func_name
        return new_f
    return check_accepts

if hasattr(select, 'poll'):
    @accepts(list, int, list)
    def wait_many_fds(fds, timeout, return_fd=None):
        """Wait for any of an arbitrary list of FDs to become ready."""
        pollster = select.poll()
        for fd in fds:
            pollster.register(fd, select.POLLIN)

        evts = pollster.poll(timeout)
        if return_fd:
            # Requires POLLHUP
