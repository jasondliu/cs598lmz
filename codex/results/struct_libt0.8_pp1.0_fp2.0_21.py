import _struct

# 十六进制转字符串
def int32(x):
    return int(0xFFFFFFFF & x)

# 字符串转十六进制
def get_int32(data):
    return int.from_bytes(data,byteorder='big')

# 保存最后一个字符串
def save_last(client_socket,message):
    with open('last_message.txt', 'w') as f:
        f.write(message)
    f.close()

# 读取最后一个字符串
def read_last():
    last_message = ''
    with open('last_message.txt',"r") as f:
        list_message = f.readlines()
        last_message = list_message[0]
    f.close()
    return last_message

# 判断是否最后一
