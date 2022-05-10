import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#show the first 3 rows of the songs table, which should be instance of the dataframe
songs_df.head(3)

#count the number of rows and columns in the table
songs_df.shape

#number of users in the dataset
users_df['user_id'].nunique()

#number of songs in the dataset
len(songs_df)

#number of artists in the dataset
len(songs_df['artist_name'].unique())

#number of different genres in the dataset
len(songs_df['genre_ids'].unique())

#unique genres
unique_genres = songs_df['genre_ids'].unique()

#number of rows in the songs df with missing genre information
len(songs_df[songs_df['genre_ids'].isnull()])

#create a list of all the songs that have missing genre ids
songs_with_missing_genre_ids = songs_df
