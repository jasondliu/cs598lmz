import _struct
# Test _struct.Struct.format_size()


if __name__ == '__main__':
    fmt = 'ddd'
    for i in range(0, len(fmt)):
        s = _struct.Struct(fmt[:i])
        print(s.format, s.size)
