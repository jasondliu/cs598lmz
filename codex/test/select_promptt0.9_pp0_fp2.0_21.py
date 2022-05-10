import select
# Test select.select with a bad file number.
select.select([], [], [], None)
print("alive")
pipe_w, pipe_r = os.pipe()
for badfd in (-10, pipe_w + 1):
    if sys.platform != "win32":
        # OK to try to read from a write-only file descriptor.
        try:
            r, w, e = select.select([badfd], [], [], 0)
            print("bad fd=%d: r=%s w=%s e=%s" % (badfd, r, w, e))
        except ValueError as e:
            print("bad fd=%d: expected failure: %s" % (badfd, e))
