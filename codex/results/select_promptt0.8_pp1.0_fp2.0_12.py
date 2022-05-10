import select
# Test select.select()

def run():
    read_list = [sys.stdin]
    print ('Press enter to exit.')
    while True:
        readable, writable, exceptional = select.select(read_list, [], [])
        for s in readable:
            if s is sys.stdin:
                input = sys.stdin.readline()
                return

if __name__ == '__main__':
    run()
