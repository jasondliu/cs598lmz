import bz2
bz2.open(file)

index = pd.read_csv(
    "https://datasets.imdbws.com/title.basics.tsv.gz", 
    usecols=[0,1,2,3,4,5,6],
    sep="\t",
    low_memory=False, 
    dtype={
        "tconst":"str", 
        "titleType":"str", 
        "primaryTitle":"str", 
        "originalTitle":"str", 
        "isAdult":"str", 
        "startYear":"str", 
        "endYear":"str"
    }
)

print(index.head())
print(index.dtypes)
