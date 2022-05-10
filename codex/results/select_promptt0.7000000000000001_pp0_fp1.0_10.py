import select
# Test select.select() interface
import os, time
import select

read_list = [os.ttyname(0)]
write_list = [os.ttyname(1)]
expt_list = []
timeout = 10.0

while 1:
    (readready, writeready, exptready) = select.select(read_list, write_list, expt_list, timeout)
    if not readready and not writeready and not exptready:
        print "Timeout!"
        break
    else:
        print "readready =", readready
        print "writeready =", writeready
        print "exptready =", exptready
        if readready:
            data = os.read(0, 1024)
            print "Data read on stdin:", data
