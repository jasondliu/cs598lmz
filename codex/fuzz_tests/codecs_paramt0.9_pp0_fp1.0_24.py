import codecs
codecs.register_error('emoji', emoji.decode_emoji)

text = "🙂😱"
print(text)

print(text.encode("utf-8"))
data = "bcdefghijk"
data = b""

print(data)
# print(b"abcde".decode())
# print(data.decode())

# print(text.decode('emoji'))
