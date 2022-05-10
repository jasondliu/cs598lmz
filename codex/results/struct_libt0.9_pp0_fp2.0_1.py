import _struct


def pack():
    """Packs floats into bytes"""
    byts = _struct.pack("fl", 23.5, 6.209)
    print("byts:", byts)
    return


def unpack():
    """"Unpacks bytes into floats"""
    b_array = bytes((0x40, 0x5c, 0xcc, 0xcd, 0x40, 0x15, 0xae, 0x44))
    print("Floats:", _struct.unpack("fl", b_array))
    float_array = _struct.unpack("fl", b_array)
    print("Float arrays:", list(float_array))
    return


def main():
    """Main func."""
    #  pack()
    unpack()
    return


if __name__ == "__main__":
    main()
