import _struct
import os
import random

def read_image(index,filename):
	with open(filename,'rb') as f:
		f.seek(16+index*784,0)
		data = f.read(784)
		return _struct.unpack('784B',data)

def read_label(index,filename):
	with open(filename,'rb') as f:
		f.seek(8+index,0)
		data = f.read(1)
		return _struct.unpack('1B',data)[0]
		
def process_write_data(data,label):
	temp = data + label
	with open('data.txt','a+') as f:
		for i in range(len(temp)):
			if i == 0:
				f.write(str(temp[i]))
			else:
				f.write(','+str(temp[i]))
		f.write('\n')

def main():
	datapath = '
