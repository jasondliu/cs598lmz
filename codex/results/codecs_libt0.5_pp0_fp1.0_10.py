import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#connect to MySQL
conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="test", charset='utf8')
cursor = conn.cursor()

#read the json file
with open("dblp.json") as file:
    for line in file:
        #read the json line
        json_line = json.loads(line)

        #get the paper id
        paper_id = json_line["id"]

        #get the title
        title = json_line["title"]

        #get the year
        year = json_line["year"]

        #get the authors
        authors = json_line["authors"]

        #get the venues
        venues = json_line["venue"]

        #get the references
        references = json_line["references"]

        #get the keywords
        keywords = json_line["keywords"]

        #get the abstract
        abstract = json_line["abstract"]

        #
