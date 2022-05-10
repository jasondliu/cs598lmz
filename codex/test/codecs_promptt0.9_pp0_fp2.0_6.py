import codecs
# Test codecs.register_error
bits = {'test':lambda e:'replaceerror', 'replace':lambda e:'replaceerror'}
codecs.register_error('test', bits['test'])
codecs.lookup_error('test')
