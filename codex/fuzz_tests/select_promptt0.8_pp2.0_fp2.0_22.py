import select
# Test select.select (and thus poll) on Windows.
# Requires the existence of /tmp/spam.  In theory, this should be
# replaced with use of temporary files and the tempfile module.

try:
    p = select.poll()
    p.register(1)
    r = p.poll(0)
    r = p.poll()
    try:
        p.poll(-1)
    except ValueError:
        pass
    else:
        print('poll(-1) unexpectedly did not raise ValueErr
