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

errors_registry = \
[
  ('add-one-codepoint', "ignore", "add one codepoint"),
  ('add-two-codepoints', "replace", "add two codepoints"),
  ('add-utf-16-bytes', "ignore", "add UTF-16 byte order mark"),
  ('add-utf-32-bytes', "ignore", "add UTF-32 byte order mark"),
]

sample_text = """
Magna feugiat curae scelerisque condimentum fames elementum ridiculus odio. Ac leo auctor sed semper morbi erat vestibulum parturient et urna dictumst. Senectus vulputate ultricies aliquam aliquam senectus hymenaeos potenti vulputate porttitor. Lectus tincidunt sit per ullamcorper dictumst suspendisse malesuada. Nisl suspendisse potenti tempus et convallis nulla sit placerat vestibulum."""

for mode, error_handler, desc in errors_registry:
    print("
