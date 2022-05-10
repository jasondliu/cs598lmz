fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    code_type(fn)
except Exception as e: # pylint:disable=broad-except
    print('Exception: %s' % e)

try:
    code_type(fn)
except Exception as e: # pylint:disable=broad-except
    print('Exception: %s' % e)

try:
    code_type(fn)
except Exception as e: # pylint:disable=broad-except
    print('Exception: %s' % e)

try:
    code_type(fn)
except Exception as e: # pylint:disable=broad-except
    print('Exception: %s' % e)

try:
    code_type(fn)
except Exception as e: # pylint:disable=broad-except
    print('Exception: %s' % e)

try:
    code_type(fn)
except Exception as e: # pylint:disable=broad-except
    print('Exception: %s' % e)

try:
    code_type(fn)

