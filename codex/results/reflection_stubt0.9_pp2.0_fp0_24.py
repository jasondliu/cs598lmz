fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
_convert_named_tuple_from_dict(fn, [(), {}, []])"""


def test_convert_named_tuple_from_dict_context_manager():
    r = testdir.inline_runsource(CONVERT_NAMED_TUPLE_FROM_DICT_CM,)
    assert r.ret == 0
    r.assertoutcome(passed=1, failed=1)


def test_convert_named_tuple_from_dict_works_first_time():
    r = testdir.inline_runsource(CONVERT_NAMED_TUPLE_FROM_DICT_TM)
    assert r.ret == 0
    r.assertoutcome(passed=0, failed=1)
    r.stdout.fnmatch_lines(["*TypeError: 'str' object is not callable*"])
