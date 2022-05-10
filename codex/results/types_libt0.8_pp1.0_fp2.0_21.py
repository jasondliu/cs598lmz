import types
types.ModuleType('mpl_finance')

from mpl_finance import candlestick_ohlc

plt.style.use('ggplot')
data = pd.read_csv(r'C:\Users\Se7en\Desktop\ETH.csv')
data['Date'] = pd.to_datetime(data['Date'])
data = data.set_index('Date')
data[['Open','High','Low','Close']].plot(figsize=(12,6))
plt.show()

fig = plt.figure(figsize=(12,6))
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(data.index, data['High'])
ax1.plot(data.index, data['Low'])
ax1.plot(data.index, data['Close'])
plt.show
