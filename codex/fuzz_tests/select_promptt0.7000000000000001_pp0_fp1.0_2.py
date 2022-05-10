import select
# Test select.select
print(select.select([sys.stdin], [], [], 0.0)[0])
print(select.select([sys.stdin], [], [], 0.0)[0])


# Test selectors.DefaultSelector
my_sel = selectors.DefaultSelector()
my_sel.register(sys.stdin, selectors.EVENT_READ)

#print(my_sel.select(timeout=0.0)[0])
#print(my_sel.select(timeout=0.0)[0])
#
#for key, mask in my_sel.select():
#    if key.fileobj == sys.stdin:
#        print(sys.stdin.readline())
#    else:
#        raise Exception("Unknown fileobject!")

# Test selectors.EpollSelector
#my_sel = selectors.EpollSelector()
#my_sel.register(sys.stdin, selectors.EVENT_READ)
#print(my_sel.select(timeout=0.0)[0])
#print(my_sel.select(
