import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
codecs.lookup_error('replace_with_space')

def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)


def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')
with open('ai.json','w') as outfile:
    json.dump(i,outfile)
j=pd.read_json('ai.json')
j.to_csv('test.csv')
df_meta=

with open('test.json','w') as outfile:
    json.dump(i,outfile)
t=pd.read_json('test.json')
t.to_csv('test_data.csv')
for i in df_meta.index:
    if df_meta['asin'][i]==df
