import _struct
import _struct as struct
import codecs



def encode(o):
    return pickle.dumps(o)


def decode(s):
    return pickle.loads(s)


def s_decode(s):
    return struct.unpack(">B", s)[0]


def s_encode(o):
    return struct.pack(">B", o)


def i_encode(o):
    return struct.pack(">I", o)


def i_decode(s):
    return struct.unpack(">I", s)[0]


def l_encode(o):
    return struct.pack(">Q", o)


def l_decode(s):
    return struct.unpack(">Q", s)[0]


def f_encode(o):
    return struct.pack(">f", o)


def f_decode(s):
    return struct.unpack(">f", s)[0]


