import codecs
# Test codecs.register_error('notamperror', NotImpError)
# test = codecs.open("foo.txt", 'w', 'utf-8', errors='notamperror')


# Test codecs.register_error('notamperror', NotImpError)
# test = codecs.open("foo.txt", 'w', 'utf-8', errors='notamperror')

def make_example1():
    create_dir("foo")
    file_path = "foo/foo1.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        lines = ["line1\n", "line2\n", "line3\n"]
        f.writelines(lines)

def make_example2():
    create_dir("bar")
    file_path = "bar/bar1.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        lines = ["line1\n", "line2\n", "line3\n"]
        f.writelines(lines)

