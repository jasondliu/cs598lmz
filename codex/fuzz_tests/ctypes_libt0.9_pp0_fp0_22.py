import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("SkillPanelChecklF1")

def bytes_to_int(xbytes):
    return int.from_bytes(xbytes, byteorder='little', signed=False)

def bytes_to_int2(xbytes):
    return int.from_bytes(xbytes[:-1], byteorder='little', signed=False)

def bytes_to_int3(xbytes):
    return int.from_bytes(xbytes[:-2], byteorder='little', signed=False)

def parse_skill(s):
    try:
        if 0x0 <= int(s) <= 0xFF:
            return s
        else:
            raise ValueError
    except ValueError:
        print ("Usage: python " + sys.argv[0] + ' ' + "hex")
        print ('Usage: python ' + sys.argv[0] + " " + "SkillID")
        print ('Usage: python ' + sys.argv[0] + " " + "SkillID SkillID SkillID...")
        print ('Usage:
