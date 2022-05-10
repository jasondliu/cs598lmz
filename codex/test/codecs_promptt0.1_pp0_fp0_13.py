import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def test(encoding):
    print("TEST", encoding)
    try:
        u"\u3042".encode(encoding, "test.my_error_handler")
    except UnicodeEncodeError as err:
        print("ERROR:", err)

test("ascii")
test("latin-1")
test("utf-8")
test("utf-16")
test("utf-32")
test("iso2022_jp")
test("shift_jis")
test("euc_jp")
test("gb2312")
test("hz")
test("big5")
test("euc_kr")
test("utf-7")
test("utf-16-be")
test("utf-16-le")
test("utf-32-be")
