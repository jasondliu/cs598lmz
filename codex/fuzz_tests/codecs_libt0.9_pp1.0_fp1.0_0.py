import codecs
codecs.lookup('shift_jis')
df = pd.read_csv('data/last_hour.csv', index_col=0)
df['raw_text'] = df['raw_text'].astype('category').cat.codes + 1
_ = df.hist(figsize=(15, 15), bins=100, layout=(6, 2))
diff = df['diff_org'].values
urls = list(df['url'].values)

for i, x in enumerate(diff):
    if x > 1:
        print('{0}: {1}'.format(urls[i], x))
df['diff_org'].quantile(0.95)
df[df['diff_org'] < 2][:10]
5348 * 2 * 23 * 1e-5
5348 * 2 * 23 * 1e-5*3/2
2.5
(5348 * 2 * 23 * 1e-5*3/2) + 2.5
df_hour = df.copy()
df_hour = df_hour.resample('30T').sum()
