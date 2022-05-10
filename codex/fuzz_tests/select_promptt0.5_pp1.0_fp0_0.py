import select
# Test select.select()

while True:
    s = select.select([sys.stdin], [], [], 10)
    if s[0]:
        print "Got input"
        print sys.stdin.readline()
    else:
        print "No input"
        sys.stdout.flush()
