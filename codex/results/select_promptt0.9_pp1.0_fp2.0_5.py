import select
# Test select.select() with open file descriptors.
f1 =  open(test.test_support.TESTFN, "wb")
f2 =  open(test.test_support.TESTFN, "wb")
try:
    fd1 = f1.fileno()
    fd2 = f2.fileno()
    # Create a file descriptor list and verify that we can find the file
    # descriptors within the list.
    fd_list = select.select([fd1], [], [], 1.0)
    if type(fd_list) is tuple:
        rfds, wfds, efds = fd_list
    else:
        fd_list = [fd_list, [], []]
        rfds, wfds, efds = fd_list
    self.assert_(fd1 in rfds, "fd1 should have been in the list")
    self.assert_(fd1 not in wfds, "fd1 should not have been in the list")
    self.assert_(fd1 not in efds, "fd1 should
