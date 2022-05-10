import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
# sys.stdin = codecs.getreader('utf8')(sys.stdin.buffer)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='replace')

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='
