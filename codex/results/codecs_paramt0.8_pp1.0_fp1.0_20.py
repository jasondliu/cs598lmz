import codecs
codecs.register_error("surrogateescape", codecs.surrogateescape_error)

def bitfield2text(bitfield, bits=4):
    if not 0 <= len(bitfield) * bits <= len(chars):
        raise ValueError("Wrong input")
    chars_index = int(bitfield, 2)
    text = chars[chars_index:chars_index+len(bitfield)]
    return text

def text2bitfield(text, bits=4):
    bitfield = bin(int.from_bytes(text.encode("utf-8"), "big"))[2:].zfill(len(text)*bits)
    return bitfield

def encode(original_text, bits=4):
    if not 0 < bits < len(chars):
        raise ValueError("Wrong bits")
    padding = len(chars) - len(original_text) % len(chars)
    text = original_text + chars[0:padding]
    bitfield = text2bitfield(text, bits)
    return bitfield

def decode(bitfield, bits=
