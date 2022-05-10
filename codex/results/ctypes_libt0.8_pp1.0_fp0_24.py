import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("HEX CODE")
from os import system
from time import sleep
import readline

c = '\033[36m'

def slows(x, y):
    for i in x:
        print(f'    {c}{i}', end='')
        sleep(y)
    print()

system('cls')

slows('\t\t=================================================================\n', 0.04)
print(f'\t\t\t{c}HEX CODE')
print(f'\t\t{c}Author: {c}https://github.com/S4SID')
slows('\n\t\t=================================================================', 0.04)

while True:
    print('')
    slows('\n\t\t=================================\n\n', 0.04)
    slows(f'\t{c}[{c}1{c}] {c}HEX to TEXT\n\n\t{c}[{c}2{c}] {c}TEXT to HEX
