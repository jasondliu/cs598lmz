fn = lambda: None
# Test fn.__code__
# Same as above
fn.__code__ = codeobject
f = lambda x: x
f.__code__ = codeobject
"""

EXPECTING = """
# Scenario: f = lambda
f = lambda: None
# Scenario: fn.__code__
fn = lambda: None
# Test fn.__code__
# Same as above
fn.__code__ = codeobject
f = lambda x: x
f.__code__ = codeobject
"""

def test_program(check):
    check.result_is(CHECK_PYV)
    check.expecting(EXPECTING)
    check.run()
