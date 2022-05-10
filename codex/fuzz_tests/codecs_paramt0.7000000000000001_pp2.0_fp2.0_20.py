import codecs
codecs.register_error('skip', SkipCodec)

def load_data(path):
	return pd.read_csv(path, skipfooter=1, engine='python', encoding='utf-8-sig')
