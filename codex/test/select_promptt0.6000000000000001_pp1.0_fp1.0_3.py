import select
# Test select.select()

read_list=[server]
write_list=[]
error_list=[server]
timeout=10

readable, writeable, errored = select.select(read_list, write_list, error_list, timeout)

