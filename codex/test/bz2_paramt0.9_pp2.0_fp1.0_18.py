from bz2 import BZ2Decompressor
BZ2Decompressor

def decrypt_pwd_win(pwd, store):
    """验证win的加密密码"""
    pwd = pwd.encode('ascii')
    ret = ''
    for flag in pwd:
        if flag == b'\x00':
            text = ret
            break
        else:
            ret += chr(ord(flag) ^ store[0])
            ret_ = store[0]
            for index in range(len(store) - 1):
                store[index] = store[index + 1]
            store[len(store) - 1] = ret_
    return text


def get_dic(dic_file):
    if dic_file:
        if dic_file == '-':
            dicts = _stdin.readlines()
        else:
            dicts = open(dic_file).readlines()
        return dicts


