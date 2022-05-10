import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

conn = pymysql.connect(host='localhost', user='root', password='', db='crawl', charset='utf8mb4')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS crawl
             (id INTEGER PRIMARY KEY AUTO_INCREMENT,
             url VARCHAR(255), 
             html VARCHAR(255), 
             html_file VARCHAR(255),
             page_title VARCHAR(255),
             page_description VARCHAR(255),
             page_keywords VARCHAR(255),
             page_h1 VARCHAR(255),
             page_h2 VARCHAR(255),
             page_h3 VARCHAR(255),
             page_links TEXT,
             page_images TEXT,
             page_internal_links TEXT,
             page_external_links TEXT,
             page_canonical_link VARCHAR(
