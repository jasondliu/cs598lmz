import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
url = "http://www.twse.com.tw/fund/BFI82U?response=csv&dayDate=&weekDate=&monthDate=&type=day&syear=&eyear="
res = urlopen(url)
webContent = res.read().decode('cp65001')
webContent = webContent.replace("=","")
fw = open("C:\\Users\\cbc\\Desktop\\stock\\stock_list_forget.csv","w",encoding = 'utf8')
fw.write(webContent)
fw.close()
df = pd.read_csv("C:\\Users\\cbc\\Desktop\\stock\\stock_list_forget.csv")
df = df.drop(["證券代號"],axis=1)
df = df.set_index("證券名稱")
df = df.reindex(index=df.index[::-1])
df

df.
