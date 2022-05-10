import socket
socket.if_indextoname(6)

# import subprocess
# subproc_result1 = subprocess.run(['ifconfig', 'en0'], stdout=subprocess.PIPE)
# subproc_result2 = subprocess.run(['ifconfig', 'en1'], stdout=subprocess.PIPE)


def get_lcd_state(s):
    # 0x67 Data length
    #
    # 0x00 Check state change
    # 0x0f Check state change
    # 0x00 Unknown
    # 0x01 Unknown

    # 0x04 Data length
    #
    # 0x00 Unknown
    # 0x00 Screen brightness (starts at 0x18)
    # 0x01 Unknown
    # 0x00 Unknown
    # 0x00 Unknown
    # 0x00 Unknown
    # 0x00 Unknown
    # 0x00 Unknown
    # 0x00 Unknown
    # 0x00 Unknown
    # 0x00 Unknown
    # 0x00 Unknown
    # 0x04 Unknown (Always present)
    # 0x00 Unknown
    # 0x
