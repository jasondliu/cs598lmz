gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == '<module>'
# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == __file__

# Test generator with a loop
def gen_with_loop(n):
    i = 0
    while i < n:
        yield i
        i += 1

gi = gen_with_loop(3)
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == 'gen_with_loop'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == 'gen_with_loop'
# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co
