import select
# Test select.select().

import support
support.verbose = 0

try:
    select.select
except AttributeError:
    support.write('This test requires select.select()\n')
    support.set_errno(0)
    raise SystemExit

for (n, how) in (0, "r"), (-1, "r"), (1, "r"):
    l = []
    try:
        l = select.select(n, l, l, l)
    except TypeError:
        support.set_errno(0)
        raise SystemExit
    assert l == [], "select.select(%s, %s, %s, %s) -> %s, expected []" % \
                    (n, how, how, how, l)

# this test doesn't currently work on Windows because of
# http://bugs.python.org/issue1871
# try:
#     select.select([fd], [], [], 0)
# except select.error, (errno, strerror):
#     assert errno == errno.EINTR, '
