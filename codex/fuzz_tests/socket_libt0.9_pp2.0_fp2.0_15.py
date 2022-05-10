import socket
import struct

#输入需要查询的IP
if __name__=="__main__":
    while True:
        address = input('请输入查询字符串(输入“exit”退出查询程序):')
        if address == 'exit':
            exit()
        try:
            info = socket.getaddrinfo(address, None)
            for item in info:
                if '192.168' in item[4][0]:
                    print('地址:',item[4][0],'\n种类：',item[0],'\n协议:',item[1])
        except Exception as result:
            print('查询失败，原因%s' % result)
