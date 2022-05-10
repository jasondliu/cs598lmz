import select
# Test select.select()
read_list = []
write_list = []
error_list = []
timeout = 10

while True:
    rlist, wlist, elist = select.select(read_list, write_list, error_list, timeout)
    if rlist:
        print("rlist is readable")
    if wlist:
        print("wlist is writeable")
    if elist:
        print("elist is error")
    if not (rlist or wlist or elist):
        print("timeout...")
