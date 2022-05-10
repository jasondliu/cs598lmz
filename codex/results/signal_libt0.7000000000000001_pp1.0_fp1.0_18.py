import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Read the data
data = read_csv('datasets/data_banknote_authentication.txt',
                header=None,
                names=['variance', 'skewness', 'curtosis', 'entropy', 'class'])

# Check the data
print(data.head())
print(data.describe())

# Sort the data
data.sort_values(by='class', inplace=True)


# Plot the data
# Plot the variance
plt.clf()
plt.plot(data['variance'], 'r-')
plt.xlabel('Index')
plt.ylabel('Variance')
plt.title('Variance')
plt.savefig('plots/variance.png')
plt.clf()

# Plot the skewness
plt.plot(data['skewness'], 'g-')
plt.xlabel('Index')
plt.ylabel('Skewness')
pl
