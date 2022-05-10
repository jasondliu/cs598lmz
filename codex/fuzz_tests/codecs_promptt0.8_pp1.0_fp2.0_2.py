import codecs
# Test codecs.register_error to handle poorly encoded input
# Specifically, \xa1 (hex), which is \xc3\xa1 in utf-8,
# is not a valid ascii symbol
text = codecs.open("test.txt", encoding='latin-1', errors='strict').read()

# "test" is "t\xe9st" when latin-1 encoded
for match in re.finditer('test', text, re.IGNORECASE):
    (start, end) = match.span()
    print(start, end)

# "test" is "t\xc3\xa9st" when utf-8 encoded
for match in re.finditer('test', text.encode('utf-8'), re.IGNORECASE):
    (start, end) = match.span()
    print(start, end)

# "test" is "\xf1\xe9st" when utf-8 encoded
for match in re.finditer('test', text.encode(), re.IGNORECASE):
    (start, end) = match.span()
    print(
