import codecs
# Test codecs.register_error()

import test_support

def test(m):
    # codecs.register_error()
    def error1(e):
        return (e.object[e.start], e.start+1)

    print codecs.replace_errors(u"abc\x80\x80\x81\x81def\xc0\xc0\xc1\xc1", error1)


if __name__ == "__main__":
    test_support.run_unittest(__name__)
