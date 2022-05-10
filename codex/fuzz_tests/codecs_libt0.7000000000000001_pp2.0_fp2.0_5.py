import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

## Loaing Data from Excel
excel_path = "./data/population_prefecture_japan_2020"
df = pd.read_csv(excel_path)
#df = pd.read_csv(excel_path, encoding="SHIFT-JIS")
#df = pd.read_csv(excel_path, encoding="SHIFT-JIS", engine='python')
df

## Loading Data from Json
json_path = "./data/population_prefecture_japan_2020.json"
df = pd.read_json(json_path)
df

## Loading Data from HTML
html_path = "./data/population_prefecture_japan_2020.html"
df = pd.read_html(html_path)
df

## Loading Data from URL
url = "https://api.github.com/repos/pandas-dev/pandas/issues"
resp = requests.get(url
