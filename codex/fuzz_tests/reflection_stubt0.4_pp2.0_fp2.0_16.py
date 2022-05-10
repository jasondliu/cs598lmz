fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This is a test for a bug in the code generator.
# The following code should be generated:
#
# 	LOAD_GLOBAL		0 (fn)
# 	LOAD_CONST		1 (1)
# 	LOAD_CONST		2 (2)
# 	CALL_FUNCTION		2
# 	POP_TOP
# 	LOAD_GLOBAL		0 (fn)
# 	LOAD_CONST		3 (3)
# 	LOAD_CONST		4 (4)
# 	CALL_FUNCTION		2
# 	POP_TOP
#
# But instead the following code is generated:
#
# 	LOAD_GLOBAL		0 (fn)
# 	LOAD_CONST		1 (1)
# 	LOAD_CONST		2 (2)
# 	CALL_FUNCTION		2
# 	POP_TOP
# 	LOAD_GLOBAL		0 (fn
