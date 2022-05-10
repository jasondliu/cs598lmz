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

# Run the tests with both surrogates on and off
# (Make sure to set the coding cookie before importing test_support)
for bytes_warning in (False, True):
    print("Running with bytes_warning %r" % (bytes_warning,))
    print("=================================")
    # BytesWarning is disregarded for tac runs, use -O mode
    # to run without optimization
    p = Popen([sys.executable,
                "-X faulthandler", "-S", "-OO", "test_codecs.py"],
                stdout=PIPE, stderr=STDOUT)
    for line in p.stdout:
        line = os.fsdecode(line.strip())
        if 'BytesWarning' in line:
            continue # Ignore also "Buffer overflow in getargs"
        if isinstance(line, str):
            print(line)
        else:
            print(line.decode(sys.stdout.encoding or 'ascii', 'replace'))
    p.wait()
    assert p.returncode == 0
    print("================================
