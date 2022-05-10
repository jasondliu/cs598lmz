import codecs
codecs.register_error("replace_with_space", codecs.replace_with_space)

def replace_char(ch):
    if ch == ".":
        ch = "\u05c3"
    elif ch == ",":
        ch = "\u05be"
    elif ch == ":":
        ch = "\u05c0"
    elif ch == "\"":
        ch = "\u05f4"
    elif ch == "\\":
        ch = "\u05f3"
    return ch

def tokenize(s):
    s = s.strip()
    tokens = []
    tok = ''
    for ch in s:
        if ch == ' ':
            tokens.append(tok)
            tok  = ''
        else:
            tok += ch
    tokens.append(tok)
    return tokens

def hebrew(s, asis=False):
    if not asis:
        ret = ''
        for ch in s:
            ret += replace_char(ch)
        return ret
    else:
        s
