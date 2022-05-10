import codecs
# Test codecs.register_error

mu ='\u039c'

def test():
    errors = ( 'strict', 'replace', 'ignore' )
    for e in errors:
        for c in ['ascii', 'latin-1', 'utf-8']:
            print('Testing codecs.register_error', c, e, ':')
            codecs.register_error(e, lambda x: ('?', x.start + 1))
            try:
                print('String encoding:')
                print(mu.encode(c, e))
                print('File encoding:')
                out = io.StringIO()
                inp = io.StringIO(mu)
                codecs.getwriter(c)(out).writelines(inp)
                print(out.getvalue())
                print('Iterator encoding:')
                iterable = iter([mu])
                print(''.join(codecs.getencoder(c)(x, e) for x in iterable))
            finally:
                codecs.register_error(e, None)

# also test the error handlers on the
