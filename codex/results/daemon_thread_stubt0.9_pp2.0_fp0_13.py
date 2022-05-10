import sys, threading

def run():
    f = urllib2.urlopen('http://www.google.com')
    print f.read(100)
    
s = timeit.Timer(lambda: run())
print 'urllib2:  %.2f usec/pass' % (1000000 * s.timeit(number=100)/100)

sys.path.insert(0, '/home/home-server/src/pycurl/build/lib.linux-i686-2.4')
s = timeit.Timer(lambda: run_pycurl_global())
print 'pycurl:   %.2f usec/pass
