import ctypes
ctypes.windll.user32._adjust_window(ctypes.windll.kernel32.GetConsoleWindow(), 0xff, True, True)
import time
import argparse
import winreg
import sys, traceback
import msvcrt

parser = argparse.ArgumentParser(description='Eclipse Keymap switcher')
parser.add_argument('--preset', type=str, choices=['python', 'java'], help='Set keymap to predefined settings')
parser.add_argument('--defaults', action='store_true', help='Reset all settings to defaults')
parser.add_argument('-define', type=str, nargs='*',
                    help='''Define custom keymap settings.\n
                    Usage: eclipse-keymap-switcher -define "key=value"
                    Available keys:
                        - visual_studio_keyboard
                        - ctrl_alt_r
                        - ctrl_r
                        - ctrl_alt_up
                        - ctrl_alt_down
                        - ctrl_shift_up
                        - ctrl_shift_down
                        -
