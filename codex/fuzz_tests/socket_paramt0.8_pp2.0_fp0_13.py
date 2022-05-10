import socket
socket.if_indextoname('2')

# Разбираем полученный пакет
def parse_raw_packet(data):
    ethhead = struct.unpack('!6s6sH', data[:14])
    src_mac = binascii.hexlify(ethhead[0])
    dst_mac = binascii.hexlify(ethhead[1])
    # Добавим деление на байты
    # http://ru.stackoverflow.com/questions/458089/%D0%A4%D0%BE%D1%80%D0%BC%D0%B0%D1%82-ip-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%B8%D0%B7-%D0%BF%D0%BE%D0%
