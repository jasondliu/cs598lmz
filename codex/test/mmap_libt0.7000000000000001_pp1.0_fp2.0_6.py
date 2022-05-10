import mmap
import sys
import select
import struct
import time

# file_name = "C:/Users/natha/Documents/GitHub/Python-Git/Python/Pipe/fifo"

# file_name = "\\\\.\\pipe\\fifo"
# file_name = "\\\\.\\pipe\\fifo.pcm"

pipe_name = r'\\.\pipe\fifo'

def connect():
    pipe = win32pipe.CreateNamedPipe(pipe_name,
                        win32pipe.PIPE_ACCESS_DUPLEX,
                        win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
                        1, 65536, 65536,
                        300,
                        None)
    win32pipe.ConnectNamedPipe(pipe, None)
    return pipe

def write(pipe, data):
    win32file.WriteFile(pipe, data)

def read(pipe, size):
    return win32file.ReadFile(pipe, size)

