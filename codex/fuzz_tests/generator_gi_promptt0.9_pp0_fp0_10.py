gi = (i for i in ())
# Test gi.gi_code == <unknown code object>.  In this case, we only want
# the filename to be printed.  The following chunk of code computes the
# correct filename and should not be skipped by pytest's `skipif` based
# on sys.version_info.
co_filename = (
    '<unknown code object>'
    if isinstance(gi.gi_code, types.CodeType) and gi.gi_code.co_filename == '<unknown code object>'
    else '<function <genexpr> at 0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0>'
)

@mark.parametrize("flag,expected", [
    (True, (
        '*** SimpleException: Traceback (most recent call last):\n'
        '  File "(?P<filename>{filename}, line (?P<lineno>\d+)")\n'.format(
            filename=re.escape(co_filename)
        ) +
        '    raise SimpleException("oops!")\n'

