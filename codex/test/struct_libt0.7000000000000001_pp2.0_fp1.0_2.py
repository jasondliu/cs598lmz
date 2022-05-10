import _struct
import binascii
import re

'''
XorShift32 
入力値のxorShift32
'''
def xorShift32(x):
	global xor32_state
	x ^= x << 13
	x ^= x >> 17
	x ^= x << 5
	xor32_state = x
	return x


'''
XorShift32 
入力値のxorShift32
'''
def xorShift32_2(x):
	global xor32_state
	x ^= x << 13
	x ^= x >> 17
	x ^= x << 5
	xor32_state = x
	return x


'''
XorShift64 
入力値のxorShift64
'''
def xorShift64(x):
	global xor64_state
	x ^= x << 13
	x ^= x >> 7
	x ^= x << 17
	xor64_state = x
	return x


