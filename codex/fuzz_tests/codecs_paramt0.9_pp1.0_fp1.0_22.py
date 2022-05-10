import codecs
codecs.register_error('ignore', codecs.ignore_errors)

import argparse

controls = {
    'left': [
        0x50, 0x41, 0x44, 0x45, 0x42, 0x43, 0x46, 0x00, 0x47, 0x48
    ],
    'right': [0x4-1900 for i in range(10)],
    'up': [0x4-1800 for i in range(10)],
    'down': [0x4-1700 for i in range(10)],
    'start': [0x4-1600, 0x4-1610, 0x4-1620, 0x4-1630, 0x4-1640, 0x4-1650, 0x4-1660, 0x4-1670, 0x4-1680, 0x4-1590]
}
    
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='logs/log.txt', help='input list file')

