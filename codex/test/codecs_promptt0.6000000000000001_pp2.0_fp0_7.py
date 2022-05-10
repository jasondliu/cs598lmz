import codecs
# Test codecs.register_error("strict", lambda e: (u"�", e.end))

def test_read_file(filename):
    file = codecs.open(filename, 'rb', encoding='utf-8', errors='strict')
    try:
        return file.readlines()
    finally:
        file.close()

def test_write_file(filename, lines):
    file = codecs.open(filename, 'wb', encoding='utf-8', errors='strict')
    try:
        file.writelines(lines)
    finally:
        file.close()

def test_read_file_lines(filename):
    file = codecs.open(filename, 'rb', encoding='utf-8', errors='strict')
    try:
        return file.read()
    finally:
        file.close()

def test_write_file_lines(filename, lines):
    file = codecs.open(filename, 'wb', encoding='utf-8', errors='strict')
    try:
        file.write(lines)
    finally:
        file.close
