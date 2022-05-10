from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<3s3sHH"
s.size = Struct.calcsize(s.format)
print("加载包：", s.size)

# 创建tcp连接
tcp_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_cli.connect((ip, port))

# 打开文件
img_size = os.path.getsize(img_path)
img_offset = 0

# 发送文件
msg_size = s.size + img_size
msg_info = struct.pack(s.format, b'B', b'M', msg_size, img_offset)
# print("发送文件信息：", msg_info)
tcp_cli.send(msg_info)

with open(img_path, 'rb') as f:
    while True:
        img_cont = f.read(2048)
