import codecs
codecs.register(SJISStreamReader())

#### OPTIONAL
# Set the default encoding for all standard streams to UTF-8
if sys.stdout.encoding != UTF8:
    sys.stdout = codecs.getwriter(UTF8)(sys.stdout, 'strict')
if sys.stdin.encoding != UTF8:
    sys.stdin = codecs.getreader(UTF8)(sys.stdin, 'strict')
if sys.stderr.encoding != UTF8:
    sys.stderr = codecs.getwriter(UTF8)(sys.stderr, 'strict')

#### OPTIONAL
# Set the file system encoding to UTF-8
try:
    import locale
    utf8_locale = locale.normalize('en_US.UTF-8')
    os.environ['NLS_LANG'] = utf8_locale
except:
    pass

#### OPTIONAL
# Set the default encoding to UTF-8 when creating objects by default (e.g. file)
if sys.getdefaultencoding()
