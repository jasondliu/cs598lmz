import codecs
# Test codecs.register_error("test_error",test_error_handler)

print("*** Encoding/Decoding with Codecs")
print(codecs.encode("Hello World","rot13")) # Codecs are provided on codecs module
print(codecs.encode("Hello World","rot-13")) # Codecs are provided on codecs module
print(codecs.encode("Hey, Whats up!"))
print(codecs.encode("Hey, Whats up!",None,True))
print(codecs.decode("Svool Vbir","rot13").encode("utf-8"))
print(codecs.encode("€ −", "rot_13"))
print(codecs.encode("€ −","rot-13"))
print(codecs.encode("€ −", "rot13"))
print(codecs.decode("Arj Znp","rot13").encode("utf-8"))

print("\n\n")

print("**** Dict Comprehensions")
a = {1:1,2:2,3:3}
b = {
