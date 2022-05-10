import codecs
codecs.register_error("strict", codecs.ignore_errors)

@command("encode")
@command("decode")
def encode(arg):
    if arg == "":
        print("Usage: encode/decode [charset] [string]")
        return
    charset = "utf-8"
    args = arg.split(" ")
    if len(args) == 2:
        charset, arg = args
    elif len(args) > 2:
        print("Usage: encode/decode [charset] [string]")
        return
    for code in ("ascii", "utf-8", "utf-16", "hex", "base64"):
        if code in charset:
            if code == "ascii":
                arg = arg.encode("ascii", "strict")
            else:
                arg = getattr(codecs, code + "_decode")(arg)[0]
            print(code, arg)
            return
    try:
        arg = arg.encode(charset, "strict")
        print
