fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def test_percent_encode():
    assert percent_encode("http://www.example.com/") == "http%3A%2F%2Fwww.example.com%2F"
    assert percent_encode("http://www.example.com/foo=bar&baz=qux") == "http%3A%2F%2Fwww.example.com%2Ffoo%3Dbar%26baz%3Dqux"
    assert percent_encode("http://www.example.com/foo[]=bar&foo[]=baz") == "http%3A%2F%2Fwww.example.com%2Ffoo%5B%5D%3Dbar%26foo%5B%5D%3Dbaz"


def test_percent_encode_raw():
    assert percent_encode("http://www.example.com/", True) == "http://www.example.com/"
    assert percent_encode("http://www.example.com/foo=bar&baz=qux", True) == "http
