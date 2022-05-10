from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = lambda self, data: data

import serial
import time
import sys

def send_serial(data, baudrate):
    ser = serial.Serial(SERIAL_PORT, baudrate, timeout=10)
    ser.write(data)
    ser.close()


def get_serial(baudrate):
    ser = serial.Serial(SERIAL_PORT, baudrate, timeout=10)
    data = ''
    while True:
        c = ser.read()
        if c == '':
            break
        data += c
    ser.close()
    return data

def cmd_get(cmds):
    cmd = cmds[0]
    cmds = cmds[1:]
    if cmd == 'baudrate':
        return BAUDRATE
    elif cmd == 'mode':
        return MODE
    elif cmd == 'cmds':
        return CMD_LIST
    elif cmd == 'bz2':
        return BZ2_PART.decode('base64')
    elif cmd == 'size':
