import select
# Test select.select
# Note that if the kernel uses edge-triggering,
# one repetition of the test may pass when it
# should fail.
# See /lib/modules/2.6.23.13-65-default/kernel/fs/nfsd/nfsfh.c
# --Hans Reiser
# nfds=10
# input=[ select.random.randrange(1, nfds+1) for _ in xrange(nfds) ]
# output=filtered(input)
# for _ in xrange(10):
#    for fd in input: os.read(fd, 0)
#    for fd in output: os.write(output, '')
#    for fd in input: os.read(fd, 0)
#    for fd in output: os.write(output, '')
# for fd in input: os.close(fd)
# for fd in output: os.close(fd)
#
# Why not just use the two:
# - socketpair
# - open(..., O_DIRECT|O_NONBL
