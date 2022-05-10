import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 读取数据
train_data = pd.read_csv(train_path, encoding = 'cp65001')
test_data = pd.read_csv(test_path, encoding = 'cp65001')
df_output = pd.read_csv(output_path, encoding = 'cp65001')

# 提取特征集
tags = test_data['parentNodeName']
# 统计在训练集中出现次数
tags_counts = tags.value_counts()

# 根据出现次数进行排序
# 返回出现次数前10的标签，构成字典
tags_sort = tags_counts.sort_values
