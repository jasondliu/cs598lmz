import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
df = pd.read_csv("C:/Data/Capstone/Final/parsed_recipes.csv", low_memory=False)
ingredient_df = df.groupby("ingredient").filter(lambda x: len(x) > 20) #we're only selecting ingredients that are present in at least 20 recipes
ingredient_df["ingredient"] = ingredient_df["ingredient"].str.lower()
ingredient_df.index = range(len(ingredient_df))
df = df.drop("Unnamed: 0", axis=1)
df

ingredient_df["ingredient"] = ingredient_df["ingredient"].str.strip(" tsp").str.strip(" tsp.").str.strip(" kg").str.strip(" kg.")
ingredient_df

ingredient_df["ingredient"] = ingredient_df["ingredient"].str.strip(" tsp").str.strip(" tsp.").str.
