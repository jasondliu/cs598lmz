import select
# Test select.select()

def run():
    while True:
        rlist, wlist, xlist = select.select([sys.stdin,], [], [], 1)
        if rlist:
            s = sys.stdin.readline()
            print 'You entered', s
        else:
            print 'Nothing entered'

if __name__ == '__main__':
    run()
