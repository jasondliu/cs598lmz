import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
#sys.stdout = codecs.getwriter('cp65001')(sys.stdout.buffer, 'strict')

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='cp65001')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf
