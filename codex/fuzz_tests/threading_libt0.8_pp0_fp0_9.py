import threading
threading.stack_size(4768704)

# pylint: disable=invalid-name

def scrape(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    # get the content table
    table = soup.find('table', { 'class' : 'data' })
    rows = table.findAll('tr')

    for tr in rows:
        cols = tr.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        # get rid of empty rows
        if len(cols) > 0:
            # add the row to a list
            data.append([ele for ele in cols if ele]) # Get rid of empty values

    # delete the first row which is the table header
    del data[0]


scrape('http://www.mta.info/nyct/service/')
print "Finished scraping data"

def schedule_train(time):
    # check to see if the timer exists
    if not 'time' in schedule_train
