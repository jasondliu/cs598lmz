import codecs
# Test codecs.register_error('ignore', codecs.lookup_error('ignore'))
# sys.setdefaultencoding('utf-8')

def get_data(path):
	csv_data = csv.reader(open(path, 'rb'))
	return csv_data

def save_data(path, data):
	writer = csv.writer(open(path, 'wb'))
	writer.writerows(data)

def main():
	csv_data = get_data('data-2.csv')
	# print csv_data
	# print csv_data.next()
	# print csv_data.next()
	data = []
	for row in csv_data:
		data.append(row)
	# print data[0]
	# print data[1]
	# print data[1][1]
	# print data[1][1].decode('utf-8')
	# print data[1][1].decode('gb2312')
	# print data[1][1].decode('gbk')
	# print data
