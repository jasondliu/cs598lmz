fn = lambda: None
gi = (i for i in ())
fn.__code__ = (c for i in gi)
process_result = process_testcase(fn, (1,), {}, [], 0)
if process_result.out != [
    "Program did not return in time (timeout_secs)", 
    "timed-out on line None", 
]:
    raise Exception
print('passed')

# detect test, then infinite loop
print('\nTesting timed-out on itself')
fn = lambda: None
fn.__code__ = (c for i in ())
process_result = process_testcase(fn, (), {}, [], 0)
if process_result.out != [
    "Program did not return in time (timeout_secs)", 
    "timed-out on line 1", 
]:
    raise Exception
print('passed')

# detect test, then infinite loop
print('\nTesting timed-out on while loop')
fn = lambda: None
fn.__code__ = (c for i in ())
process_result = process_testcase(fn, (), {}, [], 0)
if process_result.out !=
