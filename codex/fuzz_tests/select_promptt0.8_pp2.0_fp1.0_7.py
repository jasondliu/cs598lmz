import select
# Test select.select()

import time

start = time.time()

while True:
    ready = select.select([sys.stdin], [], [], 2)
    if ready[0]:
        print('Input:', sys.stdin.readline())
        break
    else:
        print('No input. Moving on')
    time.sleep(1)

end = time.time()

print('Elapsed:', end - start)
