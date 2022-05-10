import select
# Test select.select(rlist, wlist, xlist)
# the rlist and wlist parameters each take a list of file descriptors to either wait to be ready for reading or writing.
# The xlist parameter is a list of file descriptors to be watched for exceptions.
# The return value is a three-member tuple containing the lists of file descriptors that are ready for reading, writing, and exceptions.

# The select function will return immediately if there are file descriptors to be read or written, or if there are no file descriptors to be read or written.

# If there are no exceptions to be read, the return value will be a pair of empty lists.

# If the file descriptors in the xlist parameter have exceptions to be read, the select function will block until the first exception is detected.

rlist, wlist, xlist = select.select([sys.stdin], [], [], 0)

for i in rlist:
    if i == sys.stdin:
        line = i.readline()
        print(line)
