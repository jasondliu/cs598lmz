import _struct
import re

def main():
    # Program counter
    pc = 0

    # List of instructions
    instructions = []

    # List of labels
    labels = {}

    # List of opcodes
    opcodes = {
        'NOP': 0x0,
        'LDV': 0x1,
        'STV': 0x2,
        'PUSH': 0x3,
        'POP': 0x4,
        'ADD': 0x5,
        'SUB': 0x6,
        'MUL': 0x7,
        'DIV': 0x8,
        'AND': 0x9,
        'OR': 0xa,
        'XOR': 0xb,
        'SHL': 0xc,
        'SHR': 0xd,
        'CMP': 0xe,
        'JMP': 0xf,
        'JE': 0x10,
        'JNE': 0x11,
        'JG': 0x12,
        'JL': 0x13,
        'JGE': 0x14,
       
