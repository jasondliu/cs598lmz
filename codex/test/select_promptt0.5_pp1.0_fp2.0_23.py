import select
# Test select.select()

def run_select(sock):
    while True:
        rlist, wlist, xlist = select.select([sock], [], [])
