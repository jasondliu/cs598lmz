gi = (i for i in ())
# Test gi.gi_code.co_filename
try:
    gi.gi_code.co_filename
except Exception as e:
    print('Exception:', e)
    print(type(e))
    print(e.args)
    print(e)
