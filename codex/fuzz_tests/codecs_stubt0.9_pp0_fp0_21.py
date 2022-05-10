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

def main():
    with open("error_handling_decoding.txt", encoding="utf-8-sig") as file:
        print(file.read())
    with open("error_handling_decoding.txt", encoding="utf-7", 
            errors="add_one_codepoint") as file:
        print(file.read(1))
    with open("error_handling_decoding.txt", encoding="shift-jis", 
            errors="ignore") as file:
        print(file.read())
    with open("error_handling_decoding.txt", encoding="utf-16", 
            errors="add_utf16_bytes") as file:
        print(file.read())
    with open("error_handling_decoding.txt", encoding="utf-32", 
            errors="add_utf32_bytes") as file:
        print(file.read())

if __name__ == '__main__':
    main()
