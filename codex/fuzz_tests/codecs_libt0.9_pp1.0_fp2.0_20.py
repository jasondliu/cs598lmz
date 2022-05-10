import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import pandas as pd
import numpy as np
import os
import re
from datetime import *



def write(data, path):
	if len(data) == 0:
		return
	colnames = data.columns.values
	file_path = os.path.join(os.getcwd(), path)

	# 如果文件存在就读取，不存在就创建空表格
	if os.path.exists(file_path):
		csv = pd.read_csv(file_path)
		if len(csv) == 0:
			data.to_csv(file_path, encoding='utf-8', index=False, header=True, mode='a')
		# 如果表格中的字段中有字段名
