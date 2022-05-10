import _struct
import array
import time

def get_byte(data, index):
    """
    get byte from data
    """
    return data[index]

def get_word(data, index):
    """
    get word from data
    """
    hi = data[index]
    lo = data[index + 1]
    return (hi << 8) + lo

def get_dword(data, index):
    """
    get dword from data
    """
    b1 = data[index]
    b2 = data[index + 1]
    b3 = data[index + 2]
    b4 = data[index + 3]
    return (b1 << 24) + (b2 << 16) + (b3 << 8) + b4

def set_byte(data, index, value):
    """
    set byte to data
    """
    data[index] = value

def set_word(data, index, value):
    """
    set word to data
    """
    data[index] = (value >> 8) & 0xff
   
