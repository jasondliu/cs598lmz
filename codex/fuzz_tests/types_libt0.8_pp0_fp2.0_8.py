import types
types.SimpleNamespace.__bases__ += (dict,)

def pd(*args):
    if len(args)==1:
        print(args[0])
    elif len(args)>1:
        for arg in args:
            print(arg,end=" ")
        print()
    sys.stdout.flush()

def assert_type(v, tp):
    assert isinstance(v, tp), "Expect <%s> but got <%s>"%(tp,type(v))

def to_bytes(v):
    if isinstance(v, str):
        return v.encode("utf8")
    else:
        return v

def from_bytes(v):
    if isinstance(v, bytes):
        return v.decode("utf8")
    else:
        return v

def fetch_content(ip, path):
    try:
        r = requests.get(
            "http://%s%s" % (ip, path),
            headers={"Host": "cshub.internal"}
        )
