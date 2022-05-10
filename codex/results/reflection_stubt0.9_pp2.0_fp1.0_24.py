fn = lambda: None
gi = (i for i in ())
fn.__code__ = entity_code
fn.__globals__ = gi

def test_code_entity():
    global x
    assert code_e
