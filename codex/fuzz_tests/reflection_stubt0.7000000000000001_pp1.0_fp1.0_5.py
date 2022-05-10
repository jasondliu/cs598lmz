fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 0, b'')
fn.__defaults__ = fn.__kwdefaults__ = None
del gi, i

_cs_re = re.compile(br'coding[:=]\s*([-\w.]+)')


def _detect_encoding(fp):
    for i in range(2):
        ln = fp.readline()

        m = _cs_re.search(ln)
        if m:
            return m.group(1).decode('ascii')
    return 'utf-8'


def _wrap(text, length=70, indent='    ', prefix=''):
    """Wrap text."""
    text = text.strip().replace('\t', '    ')
    pad = prefix + indent
    if len(prefix) < length:
        length -= len(prefix)
    return '\n'.join(pad + line for line in textwrap
