import codecs
codecs.register(lambda x: codecs.lookup('utf-8') if x=='cp65001' else None)

with open("output.txt", "w", encoding='utf8') as text_file:
    text_file.write(str(a))
