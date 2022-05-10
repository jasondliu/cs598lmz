fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
"""
    if expect == 'ok':
        to_check = '0'
    else:
        to_check = '1'
    assert run(source) == to_check


@pytest.mark.parametrize('expect', ['ok', 'error'])
def test_code_set_constants(expect):
    source = """\
from test import test_support
try:
    fn = lambda x = -1: None
    fn.__code__ = fn.__code__.replace(co_consts=(1,))
    fn()
    result = 0
except TypeError:
    result = 1
test_support.report_result(result, "Code object __code__ assignment")
"""
    if expect == 'ok':
        to_check = '0'
    else:
        to_check = '1'
    assert run(source) == to_check


def test_code_set_custom_cell():
    source = """\
from test import test_support
try:
    fn = lambda: None
   
