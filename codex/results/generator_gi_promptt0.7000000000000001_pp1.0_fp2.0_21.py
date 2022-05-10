gi = (i for i in ())
# Test gi.gi_code is <code object <genexpr>>
gi.gi_code.co_name == '<genexpr>'

def f(): pass
# Test f.__code__ is <code object f>
f.__code__.co_name == 'f'
