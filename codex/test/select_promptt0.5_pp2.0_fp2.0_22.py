import select
# Test select.select with a timeout
def timeout_select():
    rlist, wlist, xlist = select.select([], [], [], 1)
    print(rlist, wlist, xlist)

def main():
    timeout_select()

if __name__ == '__main__':
    main()
