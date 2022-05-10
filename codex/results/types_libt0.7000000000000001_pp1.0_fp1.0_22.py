import types
types.SimpleNamespace

def update_table(df, data):
    for i, row in df.iterrows():
        df.loc[i, 'latest_yield'] = data[i]['latest_yield']
        df.loc[i, 'latest_price'] = data[i]['latest_price']
    return df


def create_table(df, data):
    for i, row in df.iterrows():
        if row['Symbol'] in data.keys():
            df.loc[i, 'latest_price'] = data[row['Symbol']]['latest_price']
            df.loc[i, 'latest_yield'] = data[row['Symbol']]['latest_yield']
    return df

def get_table():
    df = pd.read_csv('pre_table.csv', index_col='Symbol')
    data = get_data()
    if df.shape[0] > len(data.keys()):
        count = df.shape[0] - len(data.keys())
        df.drop(df.
