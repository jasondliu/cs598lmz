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

failures = """¿™£¢∞¶ƒ®†¥¨ˆøπ“‘åß∂ƒ©˙∆˚¬…æ«å‘å¯œ˚∆˙©∑™´¨ˆøπ“‘≈ç√∫˜µ≤≥÷
¡™£¢∞¶ƒ®†¥¨ˆøπ“‘æ…
Ω≈ç√æ∑∏¥ˆøπ∆˙©˚¬∆∫˜µ≤≥÷åß∂ƒ©∆˚¬∫˜µæ…¿œ∑´®†¥¨ˆøπ“‘æ…ˆøπ€
Ω≈ç√æ∑∏¥ˆøπ∆˙©˚¬∆
Ω≈ç√∑∏¥ˆøπ
