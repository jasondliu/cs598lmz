import select
# Test select.select()
#
# No file descriptors, discards data
# secbase.py cannot be used at the same time, since it uses stdin
#
# This test will not even enter any application state, so it can be used
# as an example for a minimal test program of secbase.py


def fatal(msg):
    print("secctest.py: " + msg)
    sys.exit(1)


(fin, fin_fd) = 'stdin', sys.stdin.fileno()
(fout, fout_fd) = 'stdout', sys.stdout.fileno()
if fin_fd < 0:
    fatal("%s: no file descriptor" % fin)
if fout_fd < 0:
    fatal("%s: no file descriptor" % fout)


def add_chars(buf, s):
    for c in s:
        buf.append(ord(c))
    return buf


# A safe wrapper around read() and write() to avoid mixing data from
# different calls to select/select.read
