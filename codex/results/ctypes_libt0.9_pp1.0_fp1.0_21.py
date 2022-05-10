import ctypes
ctypes.windll.user32.ShowWindow(Process, 0)


#reads file and gets key words
file = open('c:\programming\term.txt', 'r')
line = file.readline()
file.close()
term = line.replace('\n','')

#checks date of file is older than 7 days
dataD = file.readline()
data = dataD
date = parser.parse(data)
d = date.strftime('%Y%m%d')
datefrom = date.fromordinal(date.today().toordinal()-8).isoformat()
today = date.today().isoformat()

#key
count = 0
keyWord = ""
url = ""
key = requests.get('https://old.reddit.com/r/netsec/search.json?q=' + term + '&restrict_sr=on&sort=new').json()
count = key['data']['dist']
keyWord = key['data']['children'][0]['data']['permalink']
url = key['data']['children'][
