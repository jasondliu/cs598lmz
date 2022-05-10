import lzma
lzma.open
context = ssl._create_unverified_context()

print('Initializing...')

# get the stock list that we have already reviewed
print('Reading the stocks checklist...')
f = open('stocklist.txt', 'r')
stocks = f.read()
f.close()

# extract the stock code
stock_code = (re.findall(r'\^([A-Z]+)\^',stocks))

# this will be our final dictionary
stock_dict = {}

# loop through all the stock codes
print('Starting the main loop...')
for count,i in enumerate(stock_code):
    print(i)
    # use yahoo finance to get the historical data
    url = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=954706800&period2=1580115200&interval=1d&events=history&crumb=x"%(i)
    print(url)
    data = pd.read_csv(url,index_col='Date',parse
