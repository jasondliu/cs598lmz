import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

def readSetting(filename, *args):
    """
    filename
    文件名称
    """
    try:
        with open(filename,"r+") as file:
            for line in file:
                for item in args:
                    if item in line:
                        value = line.split("=")[1]
                        value = value.strip()
                        return value
        return False
    except:
        return False

def writeSetting(filename, key, value):
    """
    filename
    文件名称
    key
    键
    value
    值
    """
    try:
        with open(filename,"r+") as file:
            print(file)
            lines = file.readlines()
            # print(lines)
            output = []
            for line in lines:
                if key in line:
                    output.append(key+"="+str(value)+
