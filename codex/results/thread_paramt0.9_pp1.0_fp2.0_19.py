import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1), daemon=True).start()  # 避免 ctrl+c 杀死python程序

# print('数据名称：' + dataset)
print('报告名称：{}@{}'.format(dataset, abbr))

cnf = pd.read_csv('./config.tsv', sep='\t')

n_ge = len(cnf['Gene']);
print('\n基因数：' + str(n_ge) + '\n')

df = pd.read_csv('./results/{}/{}.tsv'.format(abbr, dataset), sep='\t')

# 聚类数
df_group = df['clustering'].value_counts(sort=True)
n_clus = df_group.size
print('类别数：' + str(n_clus))

