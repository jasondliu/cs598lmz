import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def main():
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_path, "data.csv")
    file_path = os.path.abspath(os.path.realpath(file_path))
    data = pd.read_csv(file_path)
    data["Date"] = pd.to_datetime(data["Date"])
    data.set_index("Date", inplace=True)
    data.drop(["Open", "High", "Low", "Close", "Volume"], axis=1, inplace=True)
    #data.plot()
    #plt.show()
    #plt.plot(data)
    #plt.show()
    #data["Adj Close"].plot()
    #plt.show()
    #data.plot(subplots=True)
    #plt.show
