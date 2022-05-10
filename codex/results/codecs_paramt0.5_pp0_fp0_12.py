import codecs
codecs.register_error('ignore', codecs.ignore_errors)

#%%
# Import data
data = pd.read_csv('../data/raw/data_set_ALL_AML_train.txt', sep='\t', index_col=0, encoding='utf-8')
labels = pd.read_csv('../data/raw/actual.aml.txt', sep='\t', index_col=0, encoding='utf-8')
labels = labels.loc[data.index, :]

#%%
data.head()

#%%
labels.head()

#%%
# Drop columns with less than 10 nonzero values
cols = data.columns[(data != 0).sum() >= 10]
data = data.loc[:, cols]

#%%
# Remove genes with low variance
data = data.loc[:, data.var() >= data.var().mean()]

#%%
# Remove genes with low correlation with the labels
corr = data.corrwith(labels['cancer'])
corr = corr[abs(corr) >= 0.
