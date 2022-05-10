import mmap

def countIPs(logfile):
    """
    Takes an Apache style logfile, and returns a dictionary of counts
    of the number of times a given IP address has tried to access the server.
    """

    f = open(logfile, 'rb')
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) # create an mmap

    count = {} # dictionary of counts
    while mm.tell() < mm.size():
        p = mm.tell() # save current position
        start = p

        # get next line
        while True:
            c = mm.read_byte()
            p += 1
            if c == ord('\n'):
                break
        
        line = mm[start:p-1]
        
        # process line
        m = re.search(pattern='(\d+\.\d+\.\d+\.\d+) .* \[.*\] ".*"', string=line)
        if m:
            ip = m.groups()[0]
