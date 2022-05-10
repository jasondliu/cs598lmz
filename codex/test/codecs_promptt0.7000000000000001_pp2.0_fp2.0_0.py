import codecs
# Test codecs.register_error()

import io

if __name__ == '__main__':
    def handler(exception):
        return ('', exception.end)


    codecs.register_error('test', handler)
