from bz2 import BZ2Decompressor
BZ2Decompressor().decompress("BZh91AY&SY\x94$|\0\0\0\x01\x00\x00\x00\x01\x00\x08")


def http_get(url):
    _, _, host, path = url.split('/', 3)
    conn = httplib.HTTPConnection(host, port=80)
    conn.request("GET", "/" + path, None)
    return conn.getresponse()


def gen_repr(data):
    def is_ascii(c):
        return 0x20 <= ord(c) < 0x80
    r = repr(data)
    return "".join(c if is_ascii(c) else "." for c in r)


def id_dict(in_map):
    return {v: k for k, v in in_map.iteritems()}


def uri_decode(query):
    def is_safe(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '
