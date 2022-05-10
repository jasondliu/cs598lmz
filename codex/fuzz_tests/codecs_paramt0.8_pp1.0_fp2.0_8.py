import codecs
codecs.register_error('strict', codecs.ignore_errors)

# for use in jupyter notebook
%matplotlib inline
%config InlineBackend.figure_format = 'svg'
 
# Postgres info to connect
POSTGRES_ADDRESS = '127.0.0.1'## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'postgres' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES USERNAME
POSTGRES_PASSWORD = 'postgres' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES PASSWORD 
POSTGRES_DBNAME = 'transportation_db' ## CHANGE THIS TO YOUR DATABASE NAME

# A long string that contains the necessary Postgres login information
postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
.format(username=POSTGRES_USERNAME, 
        password=POSTGRES_PASSWORD,
        ip
