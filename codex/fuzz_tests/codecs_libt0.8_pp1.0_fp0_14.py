import codecs
codecs.open

#---------------------------------------------------------------------------------------------------------#
#------Some functions to create the list/dictionary that will be used by the Iris data scrapers ----------#
#---------------------------------------------------------------------------------------------------------#

#function to create the list that will become the input for the scrapers
def createlist(fname):
    with open(fname) as f:
        mylist = f.read().splitlines()
        return mylist

#function to take the text string of the input CSV file and create a dictionary from it. 
#This will be used as the input for the spider.
def createdict(fname):
    with open(fname, newline='') as csvfile:
        mydict = {}
        reader = csv.DictReader(csvfile)
        for row in reader:
            mydict[row['Query Name']] = row['Iris Query ID']
            mydict[row['Query Name']] = mydict[row['Query Name']].strip()
            mydict[row['Query Name']] = mydict[row['Query Name']].strip(' ')
        return mydict


