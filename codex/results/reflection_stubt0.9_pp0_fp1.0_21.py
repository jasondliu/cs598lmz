fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__closure__ = gi


@pytest.mark.parametrize(
    'input, output',
    [
        ('if', ('if', 'L0011', 'L0009', 'L0010', 'L0012')),
        ('if a:', ('if', 'L0012', 'L0010', 'L0011', 'L0013')),
        ('if a:');
        ('if a: else'),
        ('if a: else:'),
        ('if a: else: b'),
        ('if a: else: b\nc', 'L0014'),
        ('if a: else: b\nc\n', 'L0015'),
        ('if a:\r\n if b:\r\n  pass\nelse:\r\n pass', 'L0034'),
        ('if a:\nif b:\n pass\nelse:\n pass', 'L0027'),
        ('if a:\nif b: pass\nelse: pass', 'L0024'),
        ('if a:\nif b:\n pass\nelse:\n pass',
