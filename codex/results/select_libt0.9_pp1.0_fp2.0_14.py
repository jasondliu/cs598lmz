import select
import socket
import errno
import threading
import os
from random import *
from collections import defaultdict

#This is a collection of function that is responsible for formatting and re-formatting messages
#for the purpose of sending and recieving

#This function is responsible for forming the intermidiate message which can then be turned into
# the message that is actually sent. For example the word WRITE would be transformed into 004 WRITE with
# the 4 being the 'instruction number'
# The format of the message is 00 instruction number + message seperated by spaces
def format_message_2(instruction, message):
	#This is a table of instructions that can be used by this program
	instruction_number_table = {
		'WRITE': 4,
		'READ': 3,
		'SYN': 2,
		'ACK': 1,
		'BROADCAST': 5
	}
	instruction_number = instruction_number_table[instruction]
	print(len(str(instruction_number)))
	#This gets the instruction to correspond with the table
	zer
