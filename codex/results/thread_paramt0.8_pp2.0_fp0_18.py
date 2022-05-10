import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()


class ParseError(Exception):
    pass


def tokenize(s):
    return s.replace('(', ' ( ').replace(')', ' ) ').split()


def parse(program):
    return read_from_tokens(tokenize(program))


def read_from_tokens(tokens):
    if len(tokens) == 0:
        raise ParseError("unexpected EOF while reading")

    token = tokens.pop(0)

    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))

        tokens.pop(0) # pop off ')'
        return L

    elif token == ')':
        raise ParseError("Unexpected token: ')'")

    else:
        return atom(token)


def atom(token):
    try:
        return int(token)
    except Value
