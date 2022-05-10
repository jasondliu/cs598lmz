from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(open(fn,'rb').read()))

# ----------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------

# # Download the data
# !wget -N https://cb.lk/covid_19

# # Decompress the data
# !tar xzf /content/covid_19 -C /content

# # Check the folder
# !ls

# ----------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------

# # Load the data
# df_analyse = pd.read_csv('/content/covid_19/data/processed/COVID_small_flat_table.csv',sep=';')
# df_analyse.sort_values('date',ascending=True).head()

# ----------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------

# # Check the data
# df_analyse.head()

# ----------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------

# # Plot the data
# fig, ax = plt.subplots(figsize=(15,10))
# ax
