import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def scrap(pn):
	try:
		ret=[]
		i=0
		for i in range(pn):
			url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
			print("Scraping page "+url)
			driver=webdriver.Firefox()
			driver.get(url)
			time.sleep(5)
			driver.execute_script("window.scrollTo(0,window.scrollY+2000)")
			time.sleep(2)
			table=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]")
			
