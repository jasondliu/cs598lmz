import select
# Test select.select(), both with and without timeouts
# On some systems (e.g. Linux) select() may modify the timeout argument,
# keeping only the remainder after the first call. So call with a copy.
from test import test_support
from time import clock
if select.select in support.get_unreachable_objects():
    raise support.TestSkipped("select.select not defined")
if hasattr(select, "poll"):
    try:
        select.poll()
    except select.error:
        pass
    else:
        # If poll() works, then our test below is meaningless because
        # select() will get EINTR from the fd return and restart itself,
        # so anyone who doesn't throw an exception for EINTR will look
        # fine. It's possible that poll() is successful but not select(),
        # but for our purposes that's unlikely enough to not matter.
        raise support.TestSkipped("select.select() doesn't restart on EINTR")
read_fd, write_fd = os.pipe()
# We can't use subprocess here because we need the parent to close
