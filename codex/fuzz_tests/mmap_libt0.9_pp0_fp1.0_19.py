import mmap

DISPLAY_WAIT = 0.01

with open('input.txt', 'rb', 0) as file, mmap.mmap(file.fileno(), 0,
                                                  access=mmap.ACCESS_READ) as s:
    pos = 0
    x, y, w, h = 0, 0, 40, 40
    ex = x + w // 2
    ey = y + h // 2
    print(' ' * (40 * 8 + 4), end='\r')
    print(f'{chr(27)}[2J')
    print(chr(27) + '[H')
    print(' ' * (40 * 8 + 4), end='\r')
    try:
        while (pos < len(s)) and s[pos] != 99:
            ptr = []
            opcode = s[pos]
            one = opcode % 10
            opcode //= 10
            two = opcode % 10
            opcode //= 10
            three = opcode % 10
            opcode //= 10
            four = opcode % 10

            def
