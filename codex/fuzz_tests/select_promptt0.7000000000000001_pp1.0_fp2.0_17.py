import select
# Test select.select()

def run_select_test(timeout):
    print('Timeout:', timeout)
    rlist, wlist, xlist = select.select([], [], [], timeout)
    print('rlist', rlist)
    print('wlist', wlist)
    print('xlist', xlist)

run_select_test(0.3)
run_select_test(0.1)
run_select_test(0.1)
run_select_test(0.1)
run_select_test(0.1)
run_select_test(0.1)
run_select_test(0.1)
run_select_test(0.1)
run_select_test(0.1)
run_select_test(0.1)
run_select_test(0.1)

from time import sleep
sleep(1)
