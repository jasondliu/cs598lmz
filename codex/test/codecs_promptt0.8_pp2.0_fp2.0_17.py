import codecs
# Test codecs.register_error('test', codecs.replace_errors)
output = codecs.getencoder("euc_jp")("string", 'test')
print(output)

print("\n")

# Test codecs.register_error('test', codecs.strict_errors)
output = codecs.getencoder("euc_jp")("string", 'test')
print(output)

print("\n")

# Test codecs.register_error('test', codecs.ignore_errors)
output = codecs.getencoder("euc_jp")("string", 'test')
print(output)

print("\n")

# Test codecs.register_error('test', codecs.xmlcharrefreplace)
output = codecs.getencoder("euc_jp")("string", 'test')
print(output)

print("\n")

# Test codecs.register_error('test', codecs.backslashreplace)
output = codecs.getencoder("euc_jp")("string", 'test')
print(output)

