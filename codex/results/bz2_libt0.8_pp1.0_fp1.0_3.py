import bz2
bz2_file = bz2.BZ2File('./input/train_imp.csv.bz2')
data = pd.read_csv(bz2_file)
data.head()

## Performing the data transformations required
data['target'] = data['target'].apply(lambda x: 1 if x == 'yes' else 0)
data['ind_310_bin'] = data['ind_310_bin'].apply(lambda x: 1 if x == 'T' else 0)
data['ind_314_bin'] = data['ind_314_bin'].apply(lambda x: 1 if x == 'T' else 0)
data['ind_315_bin'] = data['ind_315_bin'].apply(lambda x: 1 if x == 'T' else 0)
data['ind_316_bin'] = data['ind_316_bin'].apply(lambda x: 1 if x == 'T' else 0)
data['ind_321_bin'] = data['ind_321_bin'].apply(lambda x: 1 if x == 'T' else 0)
data['
