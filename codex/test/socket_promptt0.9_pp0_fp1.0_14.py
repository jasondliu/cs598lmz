import socket
# Test socket.if_indextoname()

def testfunc(child):
    assert child.expect(["if_indextoname\[INADDR_ANY\] - success",
            pexpect.EOF, pexpect.TIMEOUT]) == 0, \
            "if_indextoname() failed"
    child.sendline("\n")

test = pexpect.test.TestFunctions(testfunc=testfunc)
test.run()
test.exit()
