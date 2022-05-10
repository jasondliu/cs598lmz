import codecs
codecs.register_error('replace_space', lambda e: (u'\ufffd', e.start + 1))
#sys.stdout = codecs.getwriter('utf_8')(sys.stdout.buffer, 'replace_space')

# OLD:
#sys.stdin = codecs.getreader('utf_8')(sys.stdin.buffer, 'replace_space')
#sys.stdout = codecs.getwriter('utf_8')(sys.stdout.buffer, 'replace_space')
#sys.stderr = codecs.getwriter('utf_8')(sys.stderr.buffer, 'replace_space')

# https://www.programiz.com/python-programming/methods/built-in/max
# https://www.geeksforgeeks.org/python-program-to-convert-list-of-string-into-list-of-integers/
# https://www.geeksforgeeks.org/program-count-words-file-using-dict-words/

# Largest Value in a list:
# https://www.ge
