import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# import sys
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)

# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr.buffer)

# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout.detach())
# sys.stderr = codecs.getwriter('utf8')(sys.stderr.detach())

# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf
