import codecs
codecs.register_error("ColourError", lambda exc: ("[colour escape]", exc.end))

def format_line(line, colour):
    """
    Formats a line, substituting colour escapes with ANSI escape sequences.
    """
    esc = chr(0x1b)

    end = -1
    for match in colour_re.finditer(line):
        yield line[end+1:match.start()]
        end = match.end()
        yield esc + colour(match.group(1)) + match.group(2) + esc + "0m"
    yield line[end+1:]

def format_stream(stream, colour, encoding="utf-8", errors="ColourError"):
    """
    Formats lines from a stream as they are read.
    """
    for line in stream:
        if isinstance(line, bytes):
            line = line.decode(encoding, errors)
        if line.endswith("\n"):
            line = line[:-1]
        yield from format_line(line, colour)

