import select
# Test select.select
def select_test():
    test_set = set([13,17])
    
    # maybe need to adjust, for testing only
    selTimeout = 3
    
    rlist, wlist, xlist = select.select(
        test_set,[],[],selTimeout)
    if (13 in rlist):
        print("event 13 fired")
    if (17 in rlist):
        print("event 17 fired")
            
# Test pty.fork
def pty_fork_test():
    import io
    import os
    
    # PTY session was setup by pty.fork
    master = io.open(os.ttyname(3),"r+b", closefd=False)
    slave = io.open(os.ttyname(4),"r+b", closefd=False)

    print("slave_device", slave)
    print("master_device", master)

    # Write nothing to slave - that will output to master
    slave.write(b"Hello World!\n")
    time.sleep(4)

    # When slave write nothing, no data will
