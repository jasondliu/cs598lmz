gi = (i for i in ())
# Test gi.gi_code is not available
with tm.assertRaises(AttributeError):
    gi.gi_code  # noqa

dummy_gen = (i for i in range(10))

# Test gi_frame is not available
with tm.assertRaises(AttributeError):
    dummy_gen.gi_frame  # noqa


def is_compiled(obj):
    c = type(obj).__code__
    return c.co_filename.endswith(('.pyc', '.pyo'))


@pytest.mark.skipif(IS_PYPY, reason='need really close python versions')
class TestUtils(object):

    def test_indent(self):
        buf = StringIO()
        write_border(buf, (1, 1))
        write_border(buf, (1, 2))
        write_border(buf, (2, 1))
        write_border(buf, (2, 2))
        res = buf.getvalue()

        exp = ('+---+---+\n'
               '|   |   |\
