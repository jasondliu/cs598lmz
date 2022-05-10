import lzma
lzma_decompress = lzma.decompress

if sys.version_info < (3, ):
    def msgpack_to_str(str_):
        return str_
else:
    def msgpack_to_str(str_):
        return str_.decode("utf8")


def unwrap_message(msg):
    # this should not be necessary for anything with txZMQ
    m = msgpack.unpackb(msg)
    if sys.version_info < (3, ):
        for k, v in m.iteritems():
            if isinstance(v, unicode):
                m[k] = v.encode("utf8")
    return m


def wrap_message(msg):
    if sys.version_info < (3, ):
        for k, v in msg.iteritems():
            if isinstance(v, unicode):
                msg[k] = v.encode("utf8")
    return msgpack.packb(msg)


def wrap_send(data, compress=False, encoding="utf8"):
   
