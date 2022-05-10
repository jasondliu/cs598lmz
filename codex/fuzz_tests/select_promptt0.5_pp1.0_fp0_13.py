import select
# Test select.select()

def main():
    infile = open('/tmp/foo', 'r')
    infd = infile.fileno()
    print 'infd =', infd
    outfile = open('/tmp/bar', 'w')
    outfd = outfile.fileno()
    print 'outfd =', outfd
    while True:
        print 'in select()'
        r, w, e = select.select([infd], [outfd], [])
        print 'r =', r
        print 'w =', w
        print 'e =', e
        if infd in r:
            print 'infd is readable'
            s = infile.readline()
            if not s: break
            print s,
        if outfd in w:
            print 'outfd is writable'
            outfile.write('hello\n')
            outfile.flush()
    print 'done'

main()
