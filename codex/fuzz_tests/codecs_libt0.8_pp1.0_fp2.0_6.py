import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

all_data = pd.read_csv("agg_data.csv", encoding="utf-8")
all_data["created_at"] = pd.to_datetime(all_data["created_at"], format='%Y-%m-%d %H:%M:%S')

all_data_copy = all_data.copy(deep=True)
all_data_copy = all_data_copy.drop(["created_at"], axis=1)


# how many days in total?
all_data["days"] = (all_data["created_at"] - all_data["created_at"][0]).apply(lambda x: x.days)
df_min = min(all_data["days"])
df_max = max(all_data["days"])
df_range = df_max - df_min
df_range

# what about each user?
all_data_copy["days"] = (all_data_copy["created
