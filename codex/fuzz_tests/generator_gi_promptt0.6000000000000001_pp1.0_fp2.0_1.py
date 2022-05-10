gi = (i for i in ())
# Test gi.gi_code.co_name == '<genexpr>'

gi = (i for i in ())
# Test gi.gi_code.co_name == '<genexpr>'

gi = ((i for i in ()) for i in ())
# Test gi.gi_code.co_name == '<genexpr>'

gi = ((i for i in ()) for i in ())
# Test gi.gi_code.co_name == '<genexpr>'

gi = (((i for i in ())) for i in ())
# Test gi.gi_code.co_name == '<genexpr>'

gi = (((i for i in ())) for i in ())
# Test gi.gi_code.co_name == '<genexpr>'

gi = ((((i for i in ())) for i in ()))
# Test gi.gi_code.co_name == '<genexpr>'

gi = ((((i for i in ())) for i in ()))
# Test gi.gi_code.co_name == '<genexpr>'
