import codecs
codecs.register_error('my_replace', codecs.replace_errors)
f_in = codecs.open('file_in.txt', 'rU', 'utf-8', errors='my_replace')
f_out = codecs.open('file_out.txt', 'w', 'utf-8')
contents = f_in.read()
contents = contents.replace(u'\ufffd', '?')
f_out.write(contents)
f_in.close()
f_out.close()
</code>

