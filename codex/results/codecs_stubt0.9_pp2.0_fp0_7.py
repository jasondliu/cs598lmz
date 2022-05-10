import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

import re

def get_to_bytes_regex(target):
    # compiled regular expressions are always going to be a bytes object.
    # Convert them to the appropriate target type before comparing.
    if isinstance(target, re.Pattern):
        target = bytes(target.pattern, 'latin-1')
    return target

def check_w(target, sources, encoding, pattern=b""):
    target = get_to_bytes_regex(target)
    for src in sources:
        if isinstance(src, bytes):
            for errors in ("strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
                encoded = src.decode(encoding, errors)
                if hasattr(target,"search"):
                    match = re.search(target, encoded)
                else:
                    match = encoded == target
                if match:
                    break
            else:
                break
        else:
            encoded = src
            if hasattr(target,"search"):
                #
