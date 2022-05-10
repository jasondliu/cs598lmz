import codecs
# Test codecs.register_error
# This function is called when an error occurs handling an encoding or decoding.
# The error handling name is the name of the handler to call.
# The second argument is a tuple of arguments to pass to the handler.
def codec_error_handler(error):
    if error.reason == 'bad coding':
        return (u'\ufffd', error.start + 1)
    else:
        return ('?', error.start + 1)
codecs.register_error('test.codec', codec_error_handler)

with open('stest.txt', 'r', encoding='utf-8') as f:
    for line in f:
        #print(line)
        pass

with open('stest.txt', 'r', encoding='test.codec') as f:
    for line in f:
        print(line)
