import threading
threading.stack_size(1249747)
# Compute the mean monthly precipitation for all available years
monthly_precipitation = []
for city in ('Moscow', 'Paris', 'Beijing'):
    months = []
    for year in range(2015,2018):
        monthly = pyowm.timeutils.monthly_map(
            [city], year
        )
        month_names = pyowm.timeutils.months_in(year)
        for month_name in month_names:
            try:
                rain = monthly[city][month_name]['rain']
                mean_rain = float(rain) / len(rain) if type(rain) is list and len(rain) > 0 else float('nan')
                months.append(mean_rain)
            except Exception:
                continue
    monthly_precipitation.append(months)

# Plot the precipitation in each year and each region into a stacked area chart
X=np.array([[1,2,3,4,5,6,7,8,9,10,11,12],[1,2,3
