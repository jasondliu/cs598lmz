import select
# Test select.select()

fd_set = [sys.stdin]
input = [sys.stdin]
while True:
    rlist, wlist, xlist = select.select(fd_set, [], [])
    for f in rlist:
        if f is sys.stdin:
            print("It's from stdin!\n")
            break
    print("Not from stdin!")
</code>

