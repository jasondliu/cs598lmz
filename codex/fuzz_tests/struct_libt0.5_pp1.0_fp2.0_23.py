import _struct

#
# This module implements the binary file format of the
# "Intermediate Format" (IF) used by distorm3.
#
# The IF is a binary file format, in which each instruction is
# stored in a fixed-size structure. The IF is used to store
# disassembled instructions in a file, and then later to read
# them, without having to do the disassembly again. This can be
# useful if you want to perform some operation on the instructions,
# and you want to save the time of doing the disassembly again.
#
# The IF is designed to be independent of the CPU architecture,
# and of the disassembler. This means it does not contain any
# CPU-specific information, and it does not depend on the
# disassembler's output.
#
# The IF contains the following information for each instruction:
#
# * the address of the instruction
# * the size of the instruction in bytes
# * the hexadecimal representation of the instruction
# * the instruction's mnemonic
# * the instruction's operands
# * the instruction's flow control type
#
# This file
