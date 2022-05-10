import bz2
bz2_file = bz2.BZ2File('data/2016-12-30_22-46-38.bz2')
my_data = response.read()
print(my_data)
bz2_file.close()
 
con = sqlite3.connect(database_name)
cur = con.cursor()

tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
for table in tables:
    print(table)

# Select all the rows from our table
sql_query = cur.execute('SELECT * FROM topic')

# Get the data and store it in a dataframe to make it easy for us to view
df = pd.read_sql_query(sql_query, con)

# Set the display options so we can see all of the columns
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 500)

# Print the head (top 5) of our table
print(df
