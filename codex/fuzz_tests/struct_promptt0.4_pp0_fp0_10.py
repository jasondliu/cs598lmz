import _struct
# Test _struct.Struct

def test_struct_error():
    tests = [
        (">", ""),
        ("@", ""),
        ("", ""),
        ("x", ""),
        ("@i", ""),
        ("@2i", ""),
        ("2i", ""),
        ("ii", ""),
        ("@ii", ""),
        ("@i", "x"),
        ("@i", "xxxx"),
        ("i", "xxxx"),
        ("@2i", "xxxx"),
        ("2i", "xxxx"),
        ("2i", "xxxxxxxx"),
        ("@2i", "xxxxxxxx"),
        ("ii", "xxxxxxxx"),
        ("@ii", "xxxxxxxx"),
        ("@ii", "xx"),
        ("@ii", "xxxxxx"),
        ("@2i", "xx"),
        ("2i", "xx"),
        ("@2i", "xxxxxx"),
        ("2i", "xxxxxx"),
        ("@2i", "x"*500),
        ("2i", "x"*500),
        ("@2i", "x"
