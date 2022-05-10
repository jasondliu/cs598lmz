import codecs
# Test codecs.register_error
with codecs.open('latin1_bom_aeiou.txt', 'r', 'latin-1', errors='replace') as f:
    if f.read().strip('\n') == u'\ufffd \ufffd \ufffd \ufffd \ufffd':
        print('OK')
    else:
        print('ERROR')
 
# Test non-extensible types for UTF-8
decoder = codecs.getdecoder('utf-8')
if decoder(b'a')[0] == 'a':
    print('OK')
else:
    print('ERROR')
