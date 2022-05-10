import codecs
# Test codecs.register_error("my_error", my_error_handler)
# Test codecs.register_error("my_error", my_error_handler)

def my_error_handler(exception):
    print("my_error_handler called:", exception)
    return ("", exception.start + 1)

codecs.register_error("my_error", my_error_handler)

text = b"\xff\xff"

for codec in ['ascii', 'latin1', 'utf-8']:
    print("Codec:", codec)
    try:
        print(text.decode(codec))
    except UnicodeDecodeError as ex:
        print("   UnicodeDecodeError:", ex)
    try:
        print(text.decode(codec, 'strict'))
    except UnicodeDecodeError as ex:
        print("   UnicodeDecodeError:", ex)
