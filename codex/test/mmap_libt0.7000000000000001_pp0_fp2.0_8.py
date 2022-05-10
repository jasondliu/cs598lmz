import mmap
import re

def get_header(file_path):
	header = {}
	with open(file_path, "r") as f:
		# mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
		for line_no, line in enumerate(f):
			if line_no > 1:
				break
			# match = re.search(r"^[^\s]", line)
			# if match:
			# 	print(match.group())
			# 	print(line)
			if line[0] != "#":
				print(line)
				if line_no == 0:
					line_split = line.split()
					header["table_name"] = line_split[1]
					header["file_name"] = line_split[2]
