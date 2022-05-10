gi = (i for i in ())
# Test gi.gi_code.co_name
gi.gi_code.co_name
# Test gi.gi_frame
gi.gi_frame

def f():
	return gi

# Test f().gi_code.co_name
f().gi_code.co_name
# Test f().gi_frame
f().gi_frame

# Test genexpr.gi_code.co_name
(i for i in ()).gi_code.co_name
# Test genexpr.gi_frame
(i for i in ()).gi_frame

# Test listcomp.gi_code.co_name
[i for i in ()].gi_code.co_name
# Test listcomp.gi_frame
[i for i in ()].gi_frame

# Test setcomp.gi_code.co_name
{i for i in ()}.gi_code.co_name
# Test setcomp.gi_frame
{i for i in ()}.gi_frame

# Test dictcomp.gi_code.co_name
{i:i for i in ()}.gi_code.co_name

