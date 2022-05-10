import codecs
# Test codecs.register_error("test_error",test_error_handler)

print("*** Encoding/Decoding with Codecs")
print(codecs.encode("Hello World","rot13")) # Codecs are provided on codecs module
print(codecs.encode("Hello World","rot-13")) # Codecs are provided on codecs module
print(codecs.encode("Hey, Whats up!"))
