import codecs
# Test codecs.register_error('ignore')
print '\nTest codecs.register_error(\'ignore\'):'
codecs.register_error('ignore', lambda e: ('', e.start + 1))
print codecs.register_error('ignore'), '\n'
# Test codecs.register_error('replace')
print 'Test codecs.register_error(\'replace\'):'
codecs.register_error('replace', lambda e: (u'\ufffd', e.start + 1))
print codecs.register_error('replace'), '\n'

# Test codecs.register_error('xmlcharrefreplace')
print 'Test codecs.register_error(\'xmlcharrefreplace\'):'
codecs.register_error('xmlcharrefreplace', lambda e: (u'&#%d;' % ord(e.object[e.start]), e.start + 1))
print codecs.register_error('xmlcharrefreplace'), '\n'

# Test codecs.register_error('backslashreplace')
print 'Test codecs.register_error(\'backslash
