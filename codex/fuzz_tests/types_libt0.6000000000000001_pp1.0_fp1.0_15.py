import types
types.SimpleNamespace.__repr__ = lambda self: str(self.__dict__)

def Get_Data():
    # Get the data and put it into a DataFrame
    data = pd.read_csv('data.csv')
    df = pd.DataFrame(data)
    
    # Drop the NaN values
    df = df.dropna()
    
    # Make the column names more descriptive
    df = df.rename(columns = {'Unnamed: 0': 'Date'})
    
    # Convert the date column from a string to a datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set the index to be the datetime column
    df = df.set_index('Date')
    
    return df

def Get_Daily_Returns(df):
    # Get the daily returns and put them into a DataFrame
    daily_returns = df.pct_change()
    df_daily_returns = pd.DataFrame(daily_returns)
    
    # Drop the Na
