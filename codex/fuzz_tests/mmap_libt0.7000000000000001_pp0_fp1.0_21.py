import mmap
import os
import argparse

from vgm.am29f040b import Am29F040B
from vgm.play import play, init_sdl
from vgm.processor import VgmProcessor

def main():
    parser = argparse.ArgumentParser(description='VGM music file player')
    parser.add_argument('-v', '--version', action='version', version='1.0')
    parser.add_argument('file', help='VGM file')
    parser.add_argument('-n', '--steps', help='VGM file')
    parser.add_argument('-o', '--output', default='test.wav', help='Output file')
    parser.add_argument('-s', '--silent', action='store_true', help='silent')
    parser.add_argument('-t', '--test', action='store_true', help='test')

    args = parser.parse_args()

    with open(args.file, 'rb') as f:
        data = mmap.mmap(f.fileno(), 0, mm
