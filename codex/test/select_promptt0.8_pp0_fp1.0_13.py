import select
# Test select.select()
# All writeable files are selected, but not all are writable,
# as the file objects might not actually be connected to a
# socket (use sys.stderr.fileno() to find out).  Some
# readable files are also selected, but it can't be easily
# determined which are actually readable.
read_set = [sys.stdin]
write_set = [sys.stdout, sys.stderr]
rlist, wlist, xlist = select.select(read_set, write_set, write_set)
print("rlist =", rlist)
print("wlist =", wlist)
print("xlist =", xlist)

# Test select.poll()
# All writeable files are selected, but not all are writable,
# as the file objects might not actually be connected to a
# socket (use sys.stderr.fileno() to find out).  Some
# readable files are also selected, but it can't be easily
# determined which are actually readable.
# It appears that poll() always returns sys.stdin fd even
