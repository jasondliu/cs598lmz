import select
# Test select.select()
# 2012.02.21
# Tested by Windows XP

import selector
reload(selector)

print >>sys.stderr, 'starting  ', selector.__file__

def main():
    '''main() - Test select.select()
    '''
    print '-0-0-0-0-'
    print 'Input keyboard to STDIN'
    print '-0-0-0-0-'
    list_to_watch = [sys.stdin, sys.stdout]
    timeout_in_second = 10
    result = select.select(list_to_watch,
                           [],
                           list_to_watch,
                           timeout_in_second)

    if result == ([], [], []):
        print '%d second timeout' % timeout_in_second
    else:
        print "Read from STDIN: %s" % sys.stdin.read()

if __name__ == '__main__':
    main()
