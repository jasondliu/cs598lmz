import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('utf-8'), lambda e: (u' ', e.start + 1))

# データ読み込み
data = pd.read_csv(path + '20170908_20170915_20170922_20170929_20170930_20171107_20171109.csv', encoding='utf-8',
                   header=None, error_bad_lines=False, warn_bad_lines=False, delimiter='\t')

# データを元のファイル名で統合する
for file_name, file_data in data.groupby(5):
    title = file_data.iloc[0, 4]
    article = file_data.iloc[0, 6]
    for i in file_data[7]:
        article += i
    file_data_output = pd.concat([title, article], axis=1)
    file_data_output.columns = ['title', 'article']
    file_data
