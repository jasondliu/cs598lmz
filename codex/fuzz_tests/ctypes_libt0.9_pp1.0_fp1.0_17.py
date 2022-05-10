import ctypes
ctypes.windll.user32.GetSystemMetrics(0)
# To display the total number of system pixels on the display in y direction.
ctypes.windll.user32.GetSystemMetrics(1)

# we need to make the test data stationary for the model to work properly
from statsmodels.tsa.stattools import adfuller
dftest = adfuller(df.Sales, autolag='AIC')
dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
print(dftest)
for key,value in dftest[4].items():
    dfoutput['Critical Value (%s)'%key] = value
print(dfoutput)

# The stationarity test below shows that the data is not stationary.
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(df['Sales'])
# Extract the trend, the seasonality and the residuals.
trend = decomposition.trend
seasonal
