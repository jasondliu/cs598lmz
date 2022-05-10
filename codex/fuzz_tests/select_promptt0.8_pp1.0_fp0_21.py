import select
# Test select.select(wlist, rlist, xlist)

import time

max_sleep = 3

print('  Calling select(wlist, rlist, xlist)...')
start_time = time.time()
(rin, win, xin), (rout, wout, xout) = select.select(
    [], [], [], max_sleep)
end_time = time.time()
elapsed_time = end_time - start_time

print('    select() returned in %.2f seconds' % (elapsed_time))
print('    rin = %s' % rin)
print('    win = %s' % win)
print('    xin = %s' % xin)
print('    rout = %s' % rout)
print('    wout = %s' % wout)
print('    xout = %s' % xout)
