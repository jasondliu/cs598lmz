import _struct
import sys
import re

#defining a function to parse the header and extract the information
def parse_header(header):
	header_length = struct.unpack('<B', header[0:1])[0]
	header_format = struct.unpack('<B', header[1:2])[0]
	header_data = struct.unpack('<H', header[2:4])[0]
	return header_length, header_format, header_data

#defining a function to parse the payload and extract the information
def parse_payload(payload):
	payload_format = struct.unpack('<B', payload[0:1])[0]
	payload_data = struct.unpack('<B', payload[1:2])[0]
	return payload_format, payload_data

#defining a function to check if the format is of type 0x02
def check_format(format):
	if format == 2:
		return True
	else:
		return False

#defining a function to check if the data is
