import socket
socket.if_indextoname(2)

url = "https://transparencyreport.google.com/https/certificates"
req = Request(url, headers={'User-Agent' : "Magic Browser"}) 
html = urlopen( req ).read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
table = soup.find_all('table')[0]
rows = table.find_all('tr')

all_rows = []

for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    all_rows.append(row)

print(*all_rows[1:], sep=", ")
