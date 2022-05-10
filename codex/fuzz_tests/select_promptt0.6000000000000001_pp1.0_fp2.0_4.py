import select
# Test select.select()

read_list = [sys.stdin]
write_list = []
error_list = []

timeout = 10

print "Monitoring IO ..."
readable, writable, errored = select.select(read_list, write_list, error_list, timeout)

print "Readable:", readable
print "Writable:", writable
print "Errored:", errored
